"""
Service to calculate and display estimated costs for Gemini models.
Pricing based on Gemini 2.5 public pricing (approximate).
"""

PRICING = {
    "gemini-2.5-flash-lite": {
        "input": 0.10,   # per 1M tokens
        "output": 0.40   # per 1M tokens
    },
    "gemini-2.5-pro": {
        "input": 1.25,   # per 1M tokens (< 200k context)
        "output": 10.00  # per 1M tokens (< 200k context)
    }
}

def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    """
    Calculates the estimated cost for a request.
    
    Args:
        model: The model name (e.g., "gemini-2.5-flash-lite").
        input_tokens: Number of input tokens.
        output_tokens: Number of output tokens.
        
    Returns:
        float: Estimated cost in USD.
    """
    if model not in PRICING:
        return 0.0
    
    rates = PRICING[model]
    input_cost = (input_tokens / 1_000_000) * rates["input"]
    output_cost = (output_tokens / 1_000_000) * rates["output"]
    
    return input_cost + output_cost

def format_cost(cost: float) -> str:
    """Formats the cost to 6 decimal places for micro-transactions."""
    return f"${cost:.6f}"

def report_cost_small(response_text: str, prompt_text: str = "") -> str:
    """Calculates cost for Gemini 2.5 Flash-Lite."""
    # Estimate tokens (4 chars per token approx)
    input_tokens = len(prompt_text) / 4
    output_tokens = len(response_text) / 4
    cost = estimate_cost("gemini-2.5-flash-lite", input_tokens, output_tokens)
    return f"Estimated Cost: {format_cost(cost)} (Input: ~{int(input_tokens)} tok, Output: ~{int(output_tokens)} tok)"

def report_cost_large(response_text: str, prompt_text: str = "") -> str:
    """Calculates cost for Gemini 2.5 Pro."""
    # Estimate tokens (4 chars per token approx)
    input_tokens = len(prompt_text) / 4
    output_tokens = len(response_text) / 4
    cost = estimate_cost("gemini-2.5-pro", input_tokens, output_tokens)
    return f"Estimated Cost: {format_cost(cost)} (Input: ~{int(input_tokens)} tok, Output: ~{int(output_tokens)} tok)"
