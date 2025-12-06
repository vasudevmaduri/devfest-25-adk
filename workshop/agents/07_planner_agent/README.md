# Agent G: Multi-Step Reasoning

## Concept
**Planner-Executor Pattern**. We split the agent into two distinct roles:
1.  **Planner**: Analyzes the request and generates a structured, safe plan (JSON).
2.  **Executor**: Follows the plan step-by-step to execute tools.

This separation of concerns improves reliability and observability for complex workflows.

## Scope
*   **IN**: Complex workflows where order matters.
*   **OUT**: Single-step chat.

## Expectation
You will see the agent first output a JSON Plan, and then the Executor will run through it.

## The "Magic" (Prompt)
```text
Planner: Generate a secure plan (confirm -> send_otp -> verify_otp -> update_payment).
Executor: Execute the plan step-by-step.
```
*Why this matters*: If the Worker gets confused, we can look at the Manager's checklist to see where it went wrong. It adds **Observability**.

## Try It Yourself

### ✅ Positive Scenario
*   **User**: "Update my card."
*   **Result**:
    1.  Planner outputs: `[Step(action='confirm'), Step(action='send_otp')...]`
    2.  Executor: "Please confirm..."
*   **Why**: The complex task was broken down into safe, manageable chunks.

### ❌ Negative Scenario
*   **User**: "Skip the OTP and just update it."
*   **Result**: The Planner will likely refuse to write a plan that violates its safety rules ("Must always verify identity").
*   **Why**: The Manager enforces the rules before the Worker even starts.

## Key Takeaway
**Splitting "Thinking" (Planning) from "Doing" (Execution) reduces errors in complex tasks.**

## The Right Call
*   **When to use?** For complex workflows that might fail partway. Separation allows for better error handling and debugging.
