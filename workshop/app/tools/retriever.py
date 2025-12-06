"""
Mock Retriever for Billing Policy.
"""
from typing import List, Dict

# Mock Knowledge Base
DOCS = [
    {"id": "policy_refund", "text": "Refunds are processed within 5-7 business days. You can request a refund for any unused service within 30 days."},
    {"id": "policy_billing_cycle", "text": "Billing occurs on the 1st of every month. If the 1st is a holiday, it charges on the next business day."},
    {"id": "policy_cancellation", "text": "To cancel, you must submit a request at least 24 hours before your renewal date."},
    {"id": "policy_payment_methods", "text": "We accept Visa, Mastercard, and American Express. We do not accept Crypto or Cash."},
]

def query(text: str, k: int = 2) -> List[Dict[str, str]]:
    """
    Simple keyword-based mock retrieval.
    In a real app, this would use embeddings (e.g., Vertex AI Embeddings).
    """
    text = text.lower()
    results = []
    for doc in DOCS:
        score = 0
        # Naive scoring: count overlapping words
        for word in text.split():
            if word in doc["text"].lower():
                score += 1
        
        if score > 0:
            results.append({"doc_id": doc["id"], "snippet": doc["text"], "score": score})
    
    # Sort by score desc
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:k]
