# Agent J: Large Model (High Reasoning)

## Concept
**High Capability**. Some tasks require deep reasoning, complex instruction following, or creative nuance. For these, you need a "Pro" model.

## What are we doing?
We are using **Gemini 2.5 Pro**.
*   **Cost**: ~$1.25 per 1M input tokens. (12.5x more than Flash-Lite)
*   **Capability**: High.
*   **Mechanism**: The agent uses a `finalize_response` tool to calculate the exact cost of your query and its answer before replying.

## Scope
*   **IN**: Complex logic, coding, nuanced customer support.
*   **OUT**: Simple "Hello" messages (waste of money).

## Expectation
It provides deeper, more thoughtful answers but costs significantly more.

## The "Magic" (Prompt)
We explicitly tell it:
1.  You are the "Pro" version.
2.  You **MUST** call `finalize_response` with your answer.

## Try It Yourself

### ✅ Positive Scenario (Reasoning)
*   **User**: "Analyze this complex refund policy and tell me if I qualify..."
*   **Agent**: (Gives a detailed, step-by-step analysis)
    [Estimated Cost: $0.000150 (Input: ~50 tok, Output: ~200 tok)]
*   **Why**: It has the reasoning capacity to handle complexity.

### ❌ Negative Scenario (Cost)
*   **User**: "Hi."
*   **Agent**: "Hello!
    [Estimated Cost: $0.000015 (Input: ~5 tok, Output: ~5 tok)]"
*   **Why**: Using a Pro model for simple chat is inefficient (12x more expensive than Lite).

## Key Takeaway
**Power comes at a price. Use Pro for the hard stuff, Lite for the rest.**

## The Right Call
*   **When to use?** Complex reasoning, coding, or nuance.
