from utils.llm import query_ollama

def sentiment_analyst(sentiment_data: str) -> str:
    """
    Uses LLaMA (via Ollama) to analyze market sentiment from social media, forums, etc.

    Parameters:
        sentiment_data (str): Aggregated sentiment information (positive/negative trends, sample posts, or scores).

    Returns:
        str: Summary of market sentiment with a bullish/bearish/neutral classification.
    """
    prompt = f"""
You are a market sentiment analyst.
Analyze the following social media and public sentiment data and summarize the overall market mood:

{sentiment_data}

Provide your response in the following format:
Sentiment: [Bullish / Bearish / Neutral]
Reasoning: <Your analysis and key sentiment drivers>
    """

    return query_ollama(prompt)
