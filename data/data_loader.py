import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import requests
import praw

def get_company_name(ticker: str) -> str:
    return yf.Ticker(ticker).info['longName']

def get_fundamentals(ticker: str) -> str:
    import yfinance as yf
    info = yf.Ticker(ticker).info

    try:
        summary = f'''
Company: {info.get("longName", ticker)}
Sector: {info.get("sector", "Unknown")}
Market Cap: {info.get("marketCap", "NA")}

🔍 Key Metrics:
- P/E Ratio: {info.get("trailingPE", "NA")}
- EPS (TTM): {info.get("trailingEps", "NA")}
- ROE: {info.get("returnOnEquity", "NA")}
- Debt/Equity: {info.get("debtToEquity", "NA")}
- Revenue Growth: {info.get("revenueGrowth", "NA")}
        '''
    except Exception:
        summary = f"No fundamental data found for {ticker}."

    return summary.strip()


# ---- PRICE & TECHNICAL DATA ---- #
def load_price_data(ticker: str, period: str = "3mo", interval: str = "1d") -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df["SMA_50"] = df["Close"].rolling(window=50).mean()
    df["SMA_200"] = df["Close"].rolling(window=200).mean()
    df["Return"] = df["Close"].pct_change()
    return df

# ---- SIMPLE NEWS FETCHER USING NewsAPI ---- #
NEWS_API_KEY = "a3378fe6a6414a90aa6459a18021fe5d"  # Replace with your key
def get_news_headlines(query: str, from_date: str, to_date: str) -> list:
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "sortBy": "relevancy",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        return [article["title"] for article in resp.json().get("articles", [])]
    return []

# ---- COMBINE RECENT SUMMARY ---- #
def summarize_price_for_agent(df: pd.DataFrame) -> str:
    latest = df.iloc[-1]
    trend = "above" if latest["SMA_50"] > latest["SMA_200"] else "below"
    return f"Price: {latest['Close']:.2f}, SMA-50 is {trend} SMA-200. Recent return: {latest['Return']:.2%}"


def get_last_week_dates():
    to_date = datetime.today().date()
    from_date = to_date - timedelta(days=7)
    return from_date.isoformat(), to_date.isoformat()


reddit = praw.Reddit(
    client_id="O2QQHSQUT5JRUdnHO5Sb_Q",
    client_secret="tKXGZcXffnF_4P6t-9k8UHpkx7EnHg",
    user_agent="tradingagents-bot-v1"
)

def get_reddit_mentions(keyword: str, limit=10):
    comments = []
    for submission in reddit.subreddit("all").search(keyword, sort="new", limit=limit):
        comments.append(f"{submission.title} - {submission.selftext[:200]}")
    return comments