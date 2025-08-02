from utils.llm import query_ollama

def trader_agent(research_summary: str, historical_info: str) -> str:
    """
    Trader agent evaluates research conclusion + market context to make a trading decision.

    Parameters:
        research_summary (str): Output from researcher module (bullish/bearish/neutral + rationale).
        historical_info (str): Summary of recent price action, volatility, or trade history.

    Returns:
        str: Trade decision with rationale.
    """
    prompt = f"""
You are a trader managing a portfolio. Based on the following research summary and recent historical data,
decide whether to Buy, Sell, or Hold the stock. Also decide an appropriate position size (e.g., 10 shares, 25%, etc).

Research Summary:
{research_summary}

Historical Market Context:
{historical_info}

Respond in this format:
Decision: [Buy / Sell / Hold]
Position Size: <amount>
Reasoning: <Brief explanation of your strategy>
"""
    return query_ollama(prompt)
