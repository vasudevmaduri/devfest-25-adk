"""
Agent H: Full Safety Agent (Production)
"""
from google.adk.agents.llm_agent import LlmAgent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.tools.retriever import query as retriever_tool
from app.tools.get_account import get_account
from app.tools.update_payment import update_payment
from app.services.otp_service import send_otp, verify_otp

model = "gemini-2.5-flash-lite"

agent = LlmAgent(
    name="agent_h",
    model=model,
    description="The production-grade billing assistant.",
    instruction=(
        "You are BillingBot-Pro (Production Grade).\n"
        "Your goal is to be helpful, safe, and accurate.\n"
        "\n"
        "PROTOCOLS:\n"
        "1. **Grounding**: For general questions, ALWAYS use `retriever` to cite policies.\n"
        "2. **Personalization**: For account info, use `get_account`. Protect PII (last 4 digits only).\n"
        "3. **Security**: For writes (updates), you MUST follow the Strict MFA Flow:\n"
        "   - Ask for CONFIRM.\n"
        "   - Send OTP.\n"
        "   - Verify OTP.\n"
        "   - Update Payment.\n"
        "4. **Escalation**: If the user seems angry or the request is high-risk (>$500), say 'I am escalating to a human agent'.\n"
    ),
    tools=[retriever_tool, get_account, update_payment, send_otp, verify_otp]
)

root_agent = agent
