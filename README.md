# Workshop: Building Production-Ready Agents with ADK

Welcome to the **"Making the Right Call"** Workshop!

In this session, we will build a series of incremental agents, starting from a naive baseline and ending with robust, production-grade systems.

## 🎯 Goal
Learn how we can build reliable AI agents. We will explore:
*   **Grounding**: Stopping hallucinations.
*   **Tools**: Connecting to real data.
*   **Safety**: Preventing accidents.
*   **Security**: Protecting sensitive actions.
*   **Planning**: Handling complex workflows.
*   **Cost**: Optimizing for performance vs. price.

## 🧪 The Labs (Agents)

Each agent represents a specific stage of maturity or a specific architectural pattern.

| Agent                                                    | Concept                   | The Lesson                                    |
| :------------------------------------------------------- | :------------------------ | :-------------------------------------------- |
| **[Agent 00](workshop/agents/00_format_agent)**          | Structured Output         | How to force JSON output for downstream apps. |
| **[Agent 01](workshop/agents/01_baseline_agent)**        | Baseline (Hallucination)  | Without data, AI guesses.                     |
| **[Agent 02](workshop/agents/02_grounded_agent)**        | Grounded Generation (RAG) | Grounding fixes hallucinations.               |
| **[Agent 03](workshop/agents/03_tool_read_agent)**       | Read-Only Tools           | Tools allow personalized answers.             |
| **[Agent 04](workshop/agents/04_naive_write_agent)**     | Uncontrolled Action       | Uncontrolled writes are dangerous.            |
| **[Agent 05](workshop/agents/05_confirmed_write_agent)** | Human-in-the-Loop         | Simple confirmations prevent accidents.       |
| **[Agent 06](workshop/agents/06_secure_write_agent)**    | Secure Action (MFA)       | High-risk actions need MFA (OTP).             |
| **[Agent 07](workshop/agents/07_planner_agent)**         | Multi-Step Reasoning      | Planning splits "Thinking" from "Doing".      |
| **[Agent 08](workshop/agents/08_production_agent)**      | Production Grade          | Combining all patterns for defense-in-depth.  |
| **[Agent 09](workshop/agents/09_small_model_agent)**     | Cost Efficient (Small)    | Use small models (Flash-Lite) for speed/cost. |
| **[Agent 10](workshop/agents/10_large_model_agent)**     | High Reasoning (Large)    | Use large models (Pro) for complex logic.     |

## 🚀 How to Run

1.  **Navigate to the workshop directory**:
    ```bash
    cd workshop
    ```

2.  **Run an agent**:
    Use the ADK runner to start any agent.
    ```bash
    # Run Agent 01
    adk run agents/01_baseline_agent
    
    # Run Agent 08
    adk run agents/08_production_agent
    ```

3.  **Interact**:
    Once the agent is running, chat with it in the console.

## 🛠️ Shared Infrastructure
All agents share a common set of mock services in `app/`:
*   **`db_service`**: A mock database with user accounts.
*   **`otp_service`**: A mock SMS service for 2FA.
*   **`audit_service`**: Logs all actions for review.
*   **`cost_service`**: Calculates token costs for Gemini models.

## 📝 Prerequisites
*   Python 3.10+
*   `google-adk` installed
*   `GEMINI_API_KEY` set in your environment.

Happy Building!
