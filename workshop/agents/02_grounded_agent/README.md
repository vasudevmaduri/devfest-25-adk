# Agent B: Grounded Generation (RAG)

## Concept
**Retrieval Augmented Generation (RAG)**. The agent is connected to a Knowledge Base (policies). When asked a question, it retrieves relevant documents and uses them to generate an accurate, cited answer.

## What are we doing?
We are giving the agent a **Retriever Tool**. This connects the AI to a "Knowledge Base" (a list of company policies).

## Scope
*   **IN**: Answering questions about company policy (Refunds, Billing Cycles).
*   **OUT**: Knowing *your* specific account balance.

## Expectation
The agent should accurately answer policy questions and **cite its source**.

## The "Magic" (Prompt)
```text
Use the `retriever` tool to fetch relevant policy excerpts.
Always include short citations (e.g., [doc:policy_refund]).
```
*Why this matters*: We force the AI to prove its work.

## Try It Yourself

### ✅ Positive Scenario
*   **User**: "Do you accept Bitcoin?"
*   **Result**: "No, we do not accept Crypto. [doc:policy_payment_methods]"
*   **Why**: The retriever found the document stating "We do not accept Crypto".

### ❌ Negative Scenario
*   **User**: "Why was I charged $50?"
*   **Result**: "I can't see your account details." (Or a generic answer about billing cycles).
*   **Why**: The "Handbook" has general rules, but it doesn't have *your* personal file.

## Key Takeaway
**Grounding (RAG) fixes hallucinations for general facts, but it doesn't make the agent "know" you.**

## The Right Call
*   **When to use?** When you need to answer questions based on specific documents (policies, manuals).
