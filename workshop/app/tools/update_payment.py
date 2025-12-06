"""
Tool to update payment method.
"""
from ..services.db_service import db
from ..services.audit_service import log_action

def update_payment(new_token: str, confirm: bool = False, user_id: str = "user_123") -> str:
    """
    Updates the user's payment method.
    
    Args:
        new_token: The new payment token (e.g., 'tok_123').
        confirm: Must be True to proceed.
        user_id: The user ID.
    """
    if not confirm:
        return "Error: Confirmation required. Please set confirm=True."
    
    success = db.update_payment_token(user_id, new_token)
    if success:
        log_action(user_id, "update_payment", "success", f"Updated to {new_token}")
        return "Payment method updated successfully."
    else:
        log_action(user_id, "update_payment", "failed", "User not found")
        return "Error: User not found."
