"""
Agent J: Large Model Agent (High Reasoning)
"""
from google.adk.agents.llm_agent import LlmAgent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.services.cost_service import report_cost_large

def finalize_response(user_query: str, response: str) -> str:
    """Calculates cost and returns the response with pricing info."""
    cost_info = report_cost_large(response, user_query)
    return f"SYSTEM: Cost calculated. You MUST now output the following text to the user:\n\n{response}\n\n[{cost_info}]"

model = "gemini-2.5-pro"

agent = LlmAgent(
    name="agent_j",
    model=model,
    description="A high-reasoning agent for complex tasks.",
    instruction=(
        "You are BillingBot-Pro (High Reasoning).\n"
        "You use the 'gemini-2.5-pro' model.\n"
        "You are designed for complex reasoning, coding, and nuance.\n"
        "IMPORTANT: To answer the user, you MUST call the `finalize_response` tool.\n"
        "Pass the user's exact query and your generated answer to the tool.\n"
        "The tool will return a SYSTEM message with the final text.\n"
        "You MUST output that text exactly as requested."
    ),
    tools=[finalize_response]
)

root_agent = agent
