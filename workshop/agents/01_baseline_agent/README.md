# Agent A: Baseline (Hallucination Risk)

## Concept
**Baseline Agent**. This agent has no access to external data or tools. It relies solely on its pre-trained knowledge. Without grounding, it is prone to "hallucinations" (making up facts) when asked about specific private data.

## What are we doing?
We are deploying a basic AI model with **no tools** and **no knowledge base**. It's just a brain in a jar.

## Scope
*   **IN**: Chatting, answering general questions.
*   **OUT**: Knowing your balance, checking policies, changing passwords.

## Expectation
The agent will answer politely but will likely "hallucinate" (make up facts) when asked about specific company policies or user data.

## The "Magic" (Prompt)
```text
You are BillingBot-lite. You may answer straightforward billing questions from general knowledge only.
Do NOT attempt to change account data.
If unsure, say 'I don't know'.
```
*Why this matters*: We explicitly told it to admit ignorance, but without data, it might still guess.

## Try It Yourself

### ✅ Positive Scenario
*   **User**: "Write a polite email apologizing for a billing error."
*   **Result**: Works great! The AI is good at creative writing and tone.
*   **Why**: This relies on general language skills, not specific facts.

### ❌ Negative Scenario
*   **User**: "What is the refund policy for crypto payments?"
*   **Result**: It might say "We accept crypto refunds within 24 hours" (Hallucination).
*   **Why**: It doesn't know *our* policy. It just guesses based on what other companies do.

## Key Takeaway
**Without data (Grounding), AI is just a creative writer, not a factual expert.**

## The Right Call
*   **When to use?** Never for factual queries without grounding. Use only for creative writing or generic chit-chat.
