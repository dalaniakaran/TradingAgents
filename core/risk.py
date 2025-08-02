from utils.llm import query_ollama

def risk_manager(trade_decision: str, portfolio_context: str) -> str:
    """
    Risk management agent evaluates proposed trade against portfolio and market risks.

    Parameters:
        trade_decision (str): Trader's decision output including action and position size.
        portfolio_context (str): Summary of current portfolio, risk limits, and market volatility.

    Returns:
        str: Risk decision with approval/modification/denial and rationale.
    """
    prompt = f"""
You are part of the risk management team at a trading firm.
Evaluate the following trade decision and determine if it's acceptable given the portfolio and risk environment.

Trade Decision:
{trade_decision}

Portfolio Context:
{portfolio_context}

Respond in this format:
Risk Decision: [Approve / Modify / Reject]
Reasoning: <Justification based on risk management principles>
"""
    return query_ollama(prompt)
