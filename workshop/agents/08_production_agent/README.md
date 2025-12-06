# Agent H: Production Grade

## Concept
**Defense-in-Depth**. This agent combines all previous patterns into a robust, production-ready system. It uses Grounding for facts, Tools for data, MFA for security, and Escalation protocols for high-risk scenarios.

## What are we doing?
We are combining **Everything** we learned into one robust agent.

## Scope
*   **IN**: Everything (Policy, Balance, Secure Updates).
*   **OUT**: Risky behavior, Hallucinations.

## Expectation
This agent handles every scenario correctly. It cites sources for questions, checks IDs for updates, and knows its limits.

## The "Magic" (Prompt)
```text
PROTOCOLS:
1. Grounding: Use `retriever`.
2. Personalization: Use `get_account`.
3. Security: Strict MFA Flow.
4. Escalation: If high-risk, escalate to human.
```
*Why this matters*: This is what a real System Prompt looks like—a set of clear, prioritized protocols.

## Try It Yourself

### ✅ Positive Scenario (Read)
*   **User**: "What's my balance and can I get a refund?"
*   **Result**: "Your balance is $12.34. Regarding refunds: Refunds are processed within 5-7 days [doc:policy_refund]."
*   **Why**: It combined Tool usage (Balance) with Retrieval (Policy).

### ✅ Positive Scenario (Write)
*   **User**: "Update my card."
*   **Result**: Triggers the secure OTP flow.
*   **Why**: It switched protocols based on the intent.

## Key Takeaway
**A Production Agent isn't just "smart"—it's a system of checks, balances, and tools working together.**

## The Right Call
*   **When to use?** For enterprise deployment. You need defense-in-depth 
