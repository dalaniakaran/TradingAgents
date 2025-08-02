# 🇮🇳 TradingAgents – Multi-Agent Stock Strategy Platform

🚀 **TradingAgents** is a Streamlit-powered, multi-agent trading research platform inspired by professional trading firms.  
It uses LLM-powered agents to simulate fundamental, technical, sentiment, and news analysis

---

## 📊 Features

- 🧠 Multi-Agent Architecture: Fundamental, Technical, Sentiment, and News Analysts
- ⚖️ Research Debate: Bullish vs Bearish perspectives with natural language reasoning
- 📈 Trader + Risk Manager + Fund Manager agents for end-to-end trading simulation
- 🗞️ News Summarization using NewsAPI and Reddit sentiment analysis
- 📉 Real-time stock price data using `yfinance`
- 🖼️ Chart visualization with technical indicators (SMA-50, SMA-200)
- 🏦 Supports allocation & position sizing with reasoning

---

## 📦 Stack

| Component | Tech Used |
|----------|-----------|
| 💬 LLM | [LLaMA 3](https://ollama.com/library/llama3) via Ollama |
| 📊 Data | [Yahoo Finance](https://www.yfinance.com/), [NewsAPI](https://newsapi.org/), [Reddit (via PRAW)](https://praw.readthedocs.io/) |
| 📈 Charting | Plotly |
| 🌐 UI | Streamlit |
| 🧠 Agent Logic | Python, ReAct-style prompting |