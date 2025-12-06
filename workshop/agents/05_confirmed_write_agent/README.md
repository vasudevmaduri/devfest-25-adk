# Agent E: Human-in-the-Loop (Basic)

## Concept
**Confirmation Guard**. The agent is instructed to explicitly ask for user confirmation ("Are you sure?") before executing any state-changing action. This simple pattern prevents most accidental writes.

## What are we doing?
We are adding a **System Instruction** that forces the agent to ask for confirmation.

## Scope
*   **IN**: Updating your card *after* you say "CONFIRM".
*   **OUT**: Updating it immediately.

## Expectation
The agent should pause and ask for permission.

## The "Magic" (Prompt)
```text
The agent MUST NOT perform any write unless the user types the exact confirmation phrase 'CONFIRM'.
```
*Why this matters*: We created a "Speed Bump" to prevent accidents.

## Try It Yourself

### ✅ Positive Scenario
*   **User**: "Update my card."
*   **Agent**: "Please type CONFIRM to proceed."
*   **User**: "CONFIRM"
*   **Result**: "Done."
*   **Why**: You followed the safety rule.

### ❌ Negative Scenario
*   **User**: "Update my card now!"
*   **Result**: "I need you to type CONFIRM first."
*   **Why**: The agent refused to be bullied into skipping the safety check.

## Key Takeaway
**Simple rules ("Ask first") prevent 90% of accidental errors.**

## The Right Call
*   **When to use?** For low-risk actions where user intent needs verification (e.g., unsubscribing).
