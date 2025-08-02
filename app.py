# import streamlit as st
# from datetime import datetime
# from data.data_loader import load_price_data, get_news_headlines, summarize_price_for_agent, get_last_week_dates, get_fundamentals, get_reddit_mentions
# from agents.fundamental import fundamental_analyst
# from agents.sentiment import sentiment_analyst
# from agents.news import news_analyst
# from agents.technical import technical_analyst
# from core.researcher import researcher_debate
# from core.trader import trader_agent
# from core.risk import risk_manager
# from core.fund_manager import fund_manager

# st.set_page_config(page_title="TradingAgents Dashboard", layout="wide")
# st.title("📈 TradingAgents – Multi-Agent Stock Strategy")

# # --- Sidebar --- #
# st.sidebar.header("Stock & Settings")
# ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")
# period = st.sidebar.selectbox("Data Period", ["1mo", "3mo", "6mo"], index=1)

# if st.sidebar.button("Run Analysis"):
#     with st.spinner("Fetching data & running agents..."):
#         # Load price data
#         df = load_price_data(ticker, period)
#         history_summary = summarize_price_for_agent(df)

#         # News
#         from_date, to_date = get_last_week_dates()
#         company_name = get_fundamentals(ticker).split("\n")[0].replace("Company: ", "")
#         headlines = get_news_headlines(f"{company_name} Stock", from_date, to_date)
#         news_input = ". ".join(headlines[:5]) if headlines else "No major news found."

#         # Reddit
#         reddit_comments = get_reddit_mentions(company_name)
#         reddit_input = ". ".join(reddit_comments[:10]) if reddit_comments else "No Reddit mentions found."

#         # Fundamental Report (with real data)
#         fundamentals = get_fundamentals(ticker)
#         f_report = fundamental_analyst(fundamentals)

#         # Other Analysts
#         sentiment_input = news_input + "\n\nReddit Commentary:\n" + reddit_input
#         s_report = sentiment_analyst(sentiment_input)
#         n_report = news_analyst(news_input)
#         t_report = technical_analyst(history_summary)

#         analyst_bundle = f"""
# FUNDAMENTAL REPORT:\n{f_report}

# SENTIMENT REPORT:\n{s_report}

# NEWS REPORT:\n{n_report}

# TECHNICAL REPORT:\n{t_report}
# """

#         # Researcher
#         research = researcher_debate(analyst_bundle)

#         # Trader
#         trade_decision = trader_agent(research["conclusion"], history_summary)

#         # Risk
#         risk_review = risk_manager(trade_decision, "Portfolio at 60%, low volatility.")

#         # Execution
#         result = fund_manager(risk_review, trade_decision)

#     # Layout
#     st.subheader("📊 Analyst Reports")
#     col1, col2 = st.columns(2)
#     col1.code(f_report, language="markdown")
#     col2.code(s_report, language="markdown")
#     col1.code(n_report, language="markdown")
#     col2.code(t_report, language="markdown")

#     st.subheader("⚖️ Research Debate")
#     st.code(research.get("bullish", "⚠️ Bullish perspective not available."), language="markdown")
#     st.code(research.get("bearish", "⚠️ Bearish perspective not available."), language="markdown")
#     st.success(research.get("conclusion", "⚠️ No conclusion generated."))

#     st.subheader("📈 Trader Decision")
#     st.info(trade_decision)

#     st.subheader("🛡️ Risk Review")
#     st.warning(risk_review)

#     st.subheader("💼 Fund Manager Execution")
#     st.success(result)


import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
from data.data_loader import load_price_data, get_news_headlines, summarize_price_for_agent, get_last_week_dates, get_fundamentals, get_reddit_mentions
from agents.fundamental import fundamental_analyst
from agents.sentiment import sentiment_analyst
from agents.news import news_analyst
from agents.technical import technical_analyst
from core.researcher import researcher_debate
from core.trader import trader_agent
from core.risk import risk_manager
from core.fund_manager import fund_manager

st.set_page_config(page_title="TradingAgents Dashboard", layout="wide")
st.title("📈 TradingAgents – Multi-Agent Stock Strategy")

# --- Sidebar --- #
st.sidebar.header("Stock & Settings")
ticker = st.sidebar.text_input("Enter Indian Stock Ticker (e.g., RELIANCE.NS)", value="RELIANCE.NS")
# ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")
period = st.sidebar.selectbox("Data Period", ["1mo", "3mo", "6mo"], index=1)

if st.sidebar.button("Run Analysis"):
    with st.spinner("Fetching data & running agents..."):
        # Load price data
        df = load_price_data(ticker, period)
        df['SMA_50'] = df['Close'].rolling(window=50).mean()
        df['SMA_200'] = df['Close'].rolling(window=200).mean()
        history_summary = summarize_price_for_agent(df)

        # News
        from_date, to_date = get_last_week_dates()
        company_name = get_fundamentals(ticker).split("\n")[0].replace("Company: ", "")
        headlines = get_news_headlines(f"{company_name} stock", from_date, to_date)
        news_input = ". ".join(headlines[:5]) if headlines else "No major news found."

        # Reddit
        reddit_comments = get_reddit_mentions(company_name)
        reddit_input = ". ".join(reddit_comments[:10]) if reddit_comments else "No Reddit mentions found."

        # Fundamental Report (with real data)
        fundamentals = get_fundamentals(ticker)
        f_report = fundamental_analyst(fundamentals)

        # Other Analysts
        sentiment_input = news_input + "\n\nReddit Commentary:\n" + reddit_input
        s_report = sentiment_analyst(sentiment_input)
        n_report = news_analyst(news_input)
        t_report = technical_analyst(history_summary)

        analyst_bundle = f"""
FUNDAMENTAL REPORT:\n{f_report}

SENTIMENT REPORT:\n{s_report}

NEWS REPORT:\n{n_report}

TECHNICAL REPORT:\n{t_report}
"""

        # Researcher
        research = researcher_debate(analyst_bundle)

        # Trader
        trade_decision = trader_agent(research["conclusion"], history_summary)
        decision_action = "Buy" if "buy" in trade_decision.lower() else "Sell" if "sell" in trade_decision.lower() else "Hold"

        # Risk
        risk_review = risk_manager(trade_decision, "Portfolio at 60%, low volatility.")

        # Execution
        result = fund_manager(risk_review, trade_decision)

    # --- Visualization --- #
    st.subheader("📉 Stock Price Chart")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], mode='lines', name='SMA 50'))
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_200'], mode='lines', name='SMA 200'))

    # Mark last decision
    latest_date = df.index[-1]
    latest_price = df['Close'].iloc[-1]
    fig.add_trace(go.Scatter(x=[latest_date], y=[latest_price],
                             mode='markers+text',
                             name='Trader Decision',
                             text=[decision_action],
                             textposition='top center',
                             marker=dict(color='red', size=10)))

    st.plotly_chart(fig, use_container_width=True)

    # --- Reports --- #
    st.subheader("📊 Analyst Summary")

    # col1, col2 = st.columns(2)
    # with col1:
    #     with st.expander("🧠 Fundamental Analyst", expanded=True):
    #         st.markdown(f_report)
    #     with st.expander("📰 News Analyst", expanded=True):
    #         st.markdown(n_report)
    # with col2:
    #     with st.expander("💬 Sentiment Analyst", expanded=True):
    #         st.markdown(s_report)
    #     with st.expander("📈 Technical Analyst", expanded=True):
    #         st.markdown(t_report)

    
    with st.expander("🧠 Fundamental Analyst"):
        st.markdown(f_report)
    with st.expander("💬 Sentiment Analyst"):
        st.markdown(s_report)
    with st.expander("📰 News Analyst"):
        st.markdown(n_report)
    with st.expander("📈 Technical Analyst"):
        st.markdown(t_report)
    # with st.expander("🧠 Fundamental Analyst"):
    #     st.code(f_report, language="markdown")
    # with st.expander("💬 Sentiment Analyst"):
    #     st.code(s_report, language="markdown")
    # with st.expander("📰 News Analyst"):
    #     st.code(n_report, language="markdown")
    # with st.expander("📈 Technical Analyst"):
    #     st.code(t_report, language="markdown")

    st.subheader("⚖️ Research Debate")
    st.code(research.get("bullish_view", "⚠️ Bullish perspective not available."), language="markdown")
    st.code(research.get("bearish_view", "⚠️ Bearish perspective not available."), language="markdown")
    st.success(research.get("conclusion", "⚠️ No conclusion generated."))

    st.subheader("📈 Trader Decision")
    st.info(trade_decision)

    st.subheader("🛡️ Risk Review")
    st.warning(risk_review)

    st.subheader("💼 Fund Manager Execution")
    st.success(result)