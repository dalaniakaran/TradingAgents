from utils.llm import query_ollama

def news_analyst(news_data: str) -> str:
    """
    Uses LLaMA (via Ollama) to evaluate news and macroeconomic indicators for market impact.

    Parameters:
        news_data (str): Headlines, summaries, or macroeconomic events affecting the market.

    Returns:
        str: Market impact analysis with directional insight.
    """
    prompt = f"""
You are a financial news analyst.
Based on the following news articles and macroeconomic updates, assess the potential impact on the market:

{news_data}

Provide your answer in this format:
Impact: [Positive / Negative / Neutral]
Reasoning: <Brief analysis of how these events may influence stock prices>
    """

    return query_ollama(prompt)
