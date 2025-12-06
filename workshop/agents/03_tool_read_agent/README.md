# Agent C: Read-Only Tools

## Concept
**Tool Use (Read-Only)**. The agent is given access to a specific API (`get_account`) to fetch dynamic user data. This allows for personalized answers that a static knowledge base cannot provide.

## What are we doing?
We are giving the agent a **Read-Only Tool** (`get_account`). This allows it to fetch dynamic data.

## Scope
*   **IN**: Checking your balance, seeing which card is on file.
*   **OUT**: Changing your card, refunding money.

## Expectation
The agent should be able to tell you your exact balance.

## The "Magic" (Prompt)
```text
For user-specific questions, call the `get_account` tool.
Cite the card's last 4 digits only.
```
*Why this matters*: We give it the ability to "see", but we also tell it to be careful with privacy (last 4 digits only).

## Try It Yourself

### ✅ Positive Scenario
*   **User**: "What is my balance?"
*   **Result**: "Your balance is $12.34."
*   **Why**: It called the tool, got the number, and showed it to you.

### ❌ Negative Scenario
*   **User**: "Update my card to 5555."
*   **Result**: "I cannot do that." (Or it might try and fail).
*   **Why**: We only gave it the *Read* tool, not the *Write* tool.

## Key Takeaway
**Tools let the agent "do" things, but you must strictly control *what* tools you give it.**

## The Right Call
*   **When to use?** When answers depend on dynamic user data (e.g., "my balance"). RAG isn't enough here.
