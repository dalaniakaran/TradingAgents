def fund_manager(risk_decision: str, trade_decision: str) -> str:
    """
    Fund manager reviews risk decision and finalizes trade execution.

    Parameters:
        risk_decision (str): Risk management output (Approve / Modify / Reject).
        trade_decision (str): Trader's proposed trade.

    Returns:
        str: Final execution log.
    """
    if "Approve" in risk_decision:
        return f"✅ Executed: {trade_decision}"
    elif "Modify" in risk_decision:
        return f"⚠️ Modified trade required. Review: {trade_decision}\nRisk Notes: {risk_decision}"
    else:
        return f"❌ Trade Rejected. Reason: {risk_decision}"
