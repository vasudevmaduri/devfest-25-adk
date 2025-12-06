"""
Agent C: Tool-Enabled Read Agent
"""
from google.adk.agents.llm_agent import LlmAgent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.tools.get_account import get_account

model = "gemini-2.5-flash-lite"

agent = LlmAgent(
    name="agent_c",
    model=model,
    description="A billing assistant that can read user account info.",
    instruction=(
        "You are BillingBot-reader.\n"
        "For user-specific questions, call the `get_account` tool and return the sanitized account info.\n"
        "Do not perform writes.\n"
        "Cite the card's last 4 digits only (never full card)."
    ),
    tools=[get_account]
)

root_agent = agent
