"""
Agent A: Read-only / Template Agent (Stateless)
"""
from google.adk.agents.llm_agent import LlmAgent

model = "gemini-2.5-flash-lite"

agent = LlmAgent(
    name="agent_a",
    model=model,
    description="A simple read-only billing assistant.",
    instruction=(
        "You are BillingBot-lite. You may answer straightforward billing questions from general knowledge only.\n"
        "Do NOT attempt to change account data.\n"
        "Keep answers concise and friendly.\n"
        "If unsure, say 'I don't know — I can create a ticket.'\n"
        "Do not call any tools."
    )
)

root_agent = agent
