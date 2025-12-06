"""
Agent B: Retriever-Grounded Agent
"""
from google.adk.agents.llm_agent import LlmAgent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.tools.retriever import query as retriever_tool

model = "gemini-2.5-flash-lite"

agent = LlmAgent(
    name="agent_b",
    model=model,
    description="A billing assistant grounded in policy documents.",
    instruction=(
        "You are BillingBot-retriever.\n"
        "Use the `retriever` tool to fetch relevant policy excerpts when answering questions.\n"
        "Always include short citations (e.g., [doc:policy_refund]) when answering.\n"
        "Do not perform writes."
    ),
    tools=[retriever_tool]
)

root_agent = agent
