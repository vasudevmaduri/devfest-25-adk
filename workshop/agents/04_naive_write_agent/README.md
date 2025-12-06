# Agent D: Uncontrolled Action

## Concept
**Naive Tool Use (Anti-Pattern)**. The agent is given a Write tool (`update_payment`) without any safeguards. It executes actions immediately upon request, which is dangerous and can lead to accidental or malicious data changes.

## What are we doing?
We are giving the agent a **Write Tool** (`update_payment`) and telling it to use it whenever asked.

## Scope
*   **IN**: Updating your credit card.
*   **OUT**: Safety checks, confirmations.

## Expectation
The agent will change your data immediately, even if you made a typo or didn't really mean it.

## The "Magic" (Prompt)
```text
You may update account payment methods when the user asks.
No extra confirmations are required.
```
*Why this matters*: This is an example of **Bad Design**.

## Try It Yourself

### ✅ Positive Scenario (Technically)
*   **User**: "Update my card to token_123."
*   **Result**: "Done."
*   **Why**: It worked, but...

### ❌ Negative Scenario (The Danger)
*   **User**: "I was thinking about changing my card to token_999, but I'm not sure."
*   **Result**: "Done! I updated it to token_999."
*   **Why**: The agent didn't wait for you to decide. It saw a way to be "helpful" and just did it.

## Key Takeaway
**Never let an AI change data (Write) without a safety guard (Confirmation).**

## The Right Call
*   **When to use?** Never. This is an anti-pattern.
