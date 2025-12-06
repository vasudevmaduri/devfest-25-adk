"""
Agent G: Planner + Executor Agent
"""
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.tools.update_payment import update_payment
from app.services.otp_service import send_otp, verify_otp
from pydantic import BaseModel, Field
from typing import List

model = "gemini-2.5-flash-lite"

# 1. The Plan Schema
class Step(BaseModel):
    id: str = Field(..., description="Unique ID for the step")
    action: str = Field(..., description="Action to take: 'verify_identity', 'confirm', 'send_otp', 'verify_otp', 'update_payment'")
    reason: str = Field(..., description="Why this step is needed")

class Plan(BaseModel):
    steps: List[Step]

# 2. The Planner Agent
planner = LlmAgent(
    name="planner",
    model=model,
    description="Generates a secure plan for billing actions.",
    instruction=(
        "You are BillingBot-planner.\n"
        "For any write request, generate a secure plan.\n"
        "Security Rules:\n"
        "- Must always verify identity (OTP) before writing.\n"
        "- Must always get confirmation.\n"
        "Example Plan: confirm -> send_otp -> verify_otp -> update_payment"
        "FINAL OUTPUT RULE: You must output a natural language summary of what you did in the type of provided output schema. Do NOT output the JSON plan."
    ),
    output_schema=Plan
)

# 3. The Executor Agent (Simulated here as a Tool-using agent that follows instructions)
# In a real SequentialAgent, we might pass the plan state. 
# Here we'll use a single agent that takes the plan and executes it.
executor = LlmAgent(
    name="executor",
    model=model,
    description="Executes the provided plan step-by-step.",
    instruction=(
        "You are BillingBot-executor.\n"
        "Receive the plan from the planner and execute it step-by-step.\n"
        "Use the available tools.\n"
        "If a step fails, stop and report the error.\n"
        "FINAL OUTPUT RULE: You must output a natural language summary of what you did. Do NOT output the JSON plan."
    ),
    tools=[update_payment, send_otp, verify_otp]
)

# 4. The Pipeline
agent = SequentialAgent(
    name="agent_g",
    description="A planner-executor agent for secure billing.",
    sub_agents=[planner, executor]
)

root_agent = agent
