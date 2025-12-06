# Agent 4: Structured vs Unstructured Output

This demo compares two agents performing the same complex task (Product Comparison) but with different output formats.

## The Agents

1.  **`unstructured_agent.py`**:
    *   Returns free-form text (Markdown/Paragraphs).
    *   **Pros**: Natural to read for humans.
    *   **Cons**: Difficult for software to parse, filter, or display in a custom UI.

2.  **`structured_agent.py`**:
    *   Uses `output_type=ComparisonReport` (Pydantic model).
    *   Returns a strictly typed JSON object (or Python Object).
    *   **Pros**:
        *   **UI Ready**: Can be directly mapped to a comparison table component.
        *   **Database Ready**: Can be saved to a DB without parsing.
        *   **Reliable**: The schema guarantees fields like `price` or `winner` exist.

## The Data Model (`models.py`)

We define a complex schema:
*   `Product`: Details about a single item.
*   `FeatureComparison`: A granular comparison of a specific feature (e.g., Camera).
*   `ComparisonReport`: The top-level container.

## How to Run

Run the demo script to see the simulated difference:
```bash
python demo_comparison.py
```

## Testing Prompts

Try these prompts with the agents to see how they handle different complexities:

1.  **Standard Comparison**:
    *   "Compare the Google Pixel 9 Pro and the iPhone 16 Pro."
    *   *Goal*: See how the structured agent breaks down specs vs. the unstructured narrative.

2.  **Niche Product Comparison**:
    *   "Compare the Sony WH-1000XM5 and the Bose QuietComfort Ultra Headphones."
    *   *Goal*: Verify if the agent can find specific specs (battery life, noise cancellation) and map them to the schema.

3.  **Ambiguous Request**:
    *   "Which is better, a Mac or a PC?"
    *   *Goal*: See how the structured agent forces a "winner" or "tie" in the `final_verdict` field, whereas the unstructured agent might be vague.

4.  **Multi-Product (Complex)**:
    *   "Compare the Samsung Galaxy S24 Ultra, Pixel 9 Pro, and iPhone 16 Pro."
    *   *Goal*: The current schema expects 2 products (`product_a`, `product_b`). Watch the structured agent either fail, pick the top two, or hallucinate. This is a great talking point about **Schema Limitations** in design!
