"""Agent that returns structured data."""
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .models import ComparisonReport

model = "gemini-2.5-flash-lite"

# Refactored: Single Agent with Tools
# Instead of a pipeline (where intermediate steps might be shown), 
# we use a single agent that can research AND format.

agent = LlmAgent(
    name="structured_researcher",
    model=model,
    description="Researches products and generates a structured comparison report.",
    instruction=(
        "You are a Product Research Analyst.\n"
        "1.  Receive a request to compare products.\n"
        "2.  Use the `google_search` tool to find the latest specs, prices, and reviews.\n"
        "3.  Synthesize the information.\n"
        "4.  Output the FINAL result as a `ComparisonReport` object.\n"
        "Ensure all fields in the schema are filled based on your research."
    ),
    tools=[google_search],
    output_schema=ComparisonReport
)

root_agent = agent
