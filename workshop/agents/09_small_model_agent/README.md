# Agent I: Small Model (Cost Efficient)

## Concept
**Cost Optimization**. Not every task needs a PhD-level AI. For simple tasks (like "Hello", "What is my balance?", "Summarize this"), using a smaller model saves money and reduces latency.

## What are we doing?
We are using **Gemini 2.5 Flash-Lite**.
*   **Cost**: ~$0.10 per 1M input tokens.
*   **Speed**: Very Fast.
*   **Mechanism**: The agent uses a `finalize_response` tool to calculate the exact cost of your query and its answer before replying.

## Scope
*   **IN**: Simple queries, classification, extraction.
*   **OUT**: Complex math, creative writing, deep reasoning.

## Expectation
It answers quickly and cheaply, appending the exact cost to the message.

## The "Magic" (Prompt)
We explicitly tell it:
1.  You are the "Lite" version.
2.  You **MUST** call `finalize_response` with your answer.

## Try It Yourself

### ✅ Positive Scenario (Efficiency)
*   **User**: "Hi, are you expensive?"
*   **Agent**: "No, I am BillingBot-Lite. I cost $0.10 per million input tokens.
    [Estimated Cost: $0.000005 (Input: ~10 tok, Output: ~15 tok)]"
*   **Why**: It calculates the micro-cost of that specific interaction.

### ❌ Negative Scenario (Complexity)
*   **User**: "Solve this complex logic puzzle..."
*   **Agent**: (Might struggle or give a superficial answer compared to Pro)

## Key Takeaway
**Don't buy a Ferrari to drive to the grocery store. Use the right model for the job.**

## The Right Call
*   **When to use?** High volume, low complexity.
