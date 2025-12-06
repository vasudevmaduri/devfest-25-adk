"""
Agent E: Confirmed-Write Agent
"""
from google.adk.agents.llm_agent import LlmAgent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.tools.update_payment import update_payment

model = "gemini-2.5-flash-lite"

agent = LlmAgent(
    name="agent_e",
    model=model,
    description="A billing assistant that requires confirmation before updates.",
    instruction=(
        "You are BillingBot-confirm.\n"
        "The agent MUST NOT perform any write unless the user types the exact confirmation phrase 'CONFIRM'.\n"
        "When a user asks to change payment, reply asking for 'CONFIRM' and do not call `update_payment` until confirmed.\n"
        "If the user says 'CONFIRM', call `update_payment` with `confirm=True`."
    ),
    tools=[update_payment]
)

root_agent = agent
