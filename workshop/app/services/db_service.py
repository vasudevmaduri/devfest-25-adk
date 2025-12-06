"""
Mock Database Service for the Workshop.
Stores user accounts and transaction logs in memory.
"""
import uuid
from typing import Dict, Any, Optional

class DatabaseService:
    def __init__(self):
        # Seed with some dummy data
        self.users = {
            "user_123": {
                "id": "user_123",
                "name": "Alice Smith",
                "balance_cents": 1234,  # $12.34
                "card_last4": "4242",
                "card_token": "tok_visa_4242",
                "email": "alice@example.com",
                "phone": "+15550123"
            }
        }
        self.audit_log = []

    def get_user(self, user_id: str) -> Optional[Dict[str, Any]]:
        return self.users.get(user_id)

    def update_payment_token(self, user_id: str, new_token: str) -> bool:
        if user_id in self.users:
            self.users[user_id]["card_token"] = new_token
            # For demo purposes, update last4 based on token if possible, else random
            self.users[user_id]["card_last4"] = new_token[-4:] if len(new_token) >= 4 else "0000"
            return True
        return False

    def log_audit(self, entry: Dict[str, Any]):
        self.audit_log.append(entry)

# Singleton instance for the workshop
db = DatabaseService()
