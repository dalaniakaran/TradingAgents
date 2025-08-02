from utils.llm import query_ollama

def generate_bullish_case(analyst_reports: str) -> str:
    prompt = f"""
You are a bullish researcher. Given the following analyst reports, provide a strong bullish argument for going long on the stock:

{analyst_reports}

Focus on the positive signals from fundamental, sentiment, news, and technical perspectives.
"""
    return query_ollama(prompt)

def generate_bearish_case(analyst_reports: str) -> str:
    prompt = f"""
You are a bearish researcher. Given the following analyst reports, provide a strong bearish argument against buying or holding the stock:

{analyst_reports}

Focus on the negative signals from fundamental, sentiment, news, and technical perspectives.
"""
    return query_ollama(prompt)

def summarize_debate(bullish: str, bearish: str) -> str:
    prompt = f"""
You are a neutral senior researcher. Summarize the following bullish and bearish arguments, and provide a balanced conclusion about the stock's outlook:

Bullish Argument:
{bullish}

Bearish Argument:
{bearish}

Structure your answer as:
Conclusion: [Bullish / Bearish / Neutral]
Summary: <Brief synthesis of both arguments>
"""
    return query_ollama(prompt)

def researcher_debate(analyst_reports: str) -> dict:
    """
    Full research process with bullish and bearish arguments, followed by a balanced conclusion.

    Parameters:
        analyst_reports (str): Combined output from all four analyst agents.

    Returns:
        dict: Dictionary with bullish, bearish, and final conclusion outputs.
    """
    bull = generate_bullish_case(analyst_reports)
    bear = generate_bearish_case(analyst_reports)
    summary = summarize_debate(bull, bear)
    return {
        "bullish_view": bull,
        "bearish_view": bear,
        "conclusion": summary
    }
