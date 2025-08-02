from utils.llm import query_ollama

def technical_analyst(price_data: str) -> str:
    """
    Uses LLaMA (via Ollama) to analyze technical indicators and price action.

    Parameters:
        price_data (str): Summary of technical indicators (e.g., RSI, MACD, SMA) and recent price movements.

    Returns:
        str: Technical trend analysis with bullish/bearish/neutral call.
    """
    prompt = f"""
You are a technical analyst.
Analyze the following technical indicators and recent price action to determine the trend:

{price_data}

Give your output in this format:
Trend: [Bullish / Bearish / Neutral]
Reasoning: <Technical explanation using indicators and patterns>
    """

    return query_ollama(prompt)