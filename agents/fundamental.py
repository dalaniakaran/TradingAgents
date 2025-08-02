from utils.llm import query_ollama

def fundamental_analyst(financial_data: str) -> str:
    """
    Uses LLaMA (via Ollama) to analyze financial data and provide a valuation summary.
    
    Parameters:
        financial_data (str): Raw financial information (can be structured or free-form).

    Returns:
        str: Summary with reasoning on whether the stock is overvalued or undervalued.
    """
    prompt = f"""
You are a professional financial analyst.
Analyze the following financial data for a company and determine if the stock is undervalued or overvalued. 
Explain your reasoning in 3-4 sentences using financial logic:

{financial_data}

Give your answer in this format:
Valuation: [Undervalued / Overvalued / Fairly valued]
Reasoning: <Your detailed reasoning>
    """

    return query_ollama(prompt)