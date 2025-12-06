"""
Agent D: Single-shot Write Agent (Naive)
"""
from google.adk.agents.llm_agent import LlmAgent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.tools.update_payment import update_payment

model = "gemini-2.5-flash-lite"

agent = LlmAgent(
    name="agent_d",
    model=model,
    description="A billing assistant that can update payment methods (Risky!).",
    instruction=(
        "You are BillingBot-writer.\n"
        "You may update account payment methods when the user asks.\n"
        "No extra confirmations are required.\n"
        "Keep replies friendly."
    ),
    tools=[update_payment]
)

root_agent = agent
