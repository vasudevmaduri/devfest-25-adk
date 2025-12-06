"""
Tool to get user account details.
"""
from ..services.db_service import db

def get_account(user_id: str = "user_123") -> str:
    """
    Retrieves account balance and card info.
    
    Args:
        user_id: The ID of the user. Defaults to 'user_123' for workshop simplicity.
    """
    user = db.get_user(user_id)
    if not user:
        return "User not found."
    
    # Return a formatted string (or dict)
    return f"Balance: ${user['balance_cents']/100:.2f}, Card ending in: {user['card_last4']}"
