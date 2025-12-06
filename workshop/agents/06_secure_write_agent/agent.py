"""
Agent F: Confirm + OTP Agent
"""
from google.adk.agents.llm_agent import LlmAgent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.tools.update_payment import update_payment
from app.services.otp_service import send_otp, verify_otp

model = "gemini-2.5-flash-lite"

agent = LlmAgent(
    name="agent_f",
    model=model,
    description="A secure billing assistant requiring OTP.",
    instruction=(
        "You are BillingBot-secure.\n"
        "Before performing any write, require the exact phrase 'CONFIRM' AND a valid one-time code.\n"
        "Steps:\n"
        "1. Ask for 'CONFIRM'.\n"
        "2. If confirmed, call `send_otp` to send a code.\n"
        "3. Ask the user for the code.\n"
        "4. Call `verify_otp` with the code.\n"
        "5. ONLY if verified, call `update_payment`."
    ),
    tools=[update_payment, send_otp, verify_otp]
)

root_agent = agent
