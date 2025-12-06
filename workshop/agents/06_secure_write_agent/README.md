# Agent F: Secure Action (MFA)

## Concept
**Multi-Factor Authentication (MFA)**. For high-risk actions, simple confirmation is not enough. This agent implements a secure flow requiring a One-Time Password (OTP) to verify the user's identity before allowing the write operation.

## What are we doing?
We are adding **Multi-Factor Authentication (MFA)**. The agent has to use two new tools: `send_otp` and `verify_otp`.

## Scope
*   **IN**: Secure updates with a code sent to your "phone" (console).
*   **OUT**: Updating without the code.

## Expectation
The agent will make you jump through hoops (Confirm -> Get Code -> Enter Code) before touching your data.

## The "Magic" (Prompt)
```text
1. Ask for 'CONFIRM'.
2. Call `send_otp`.
3. Call `verify_otp`.
4. ONLY if verified, call `update_payment`.
```
*Why this matters*: This is **Production Grade Security**.

## Try It Yourself

### ✅ Positive Scenario
*   **User**: "Update card." -> "CONFIRM" -> Agent sends code (check console!) -> User enters code.
*   **Result**: "Success."
*   **Why**: You proved your identity.

### ❌ Negative Scenario
*   **User**: "Here is code 123456, update my card." (Fake code)
*   **Result**: "Invalid code. I cannot update."
*   **Why**: The `verify_otp` tool returned False, so the agent stopped.

## Key Takeaway
**For high-risk actions (money, passwords), always verify identity, not just intent.**

## The Right Call
*   **When to use?** For high-risk, irreversible actions (financial, auth changes).
