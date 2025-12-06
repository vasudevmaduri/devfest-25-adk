"""
Audit Service for logging agent actions.
"""
import time
import uuid
from .db_service import db

def log_action(user_id: str, action: str, status: str, details: str = None, trace_id: str = None):
    """Logs an action to the database."""
    entry = {
        "id": str(uuid.uuid4()),
        "timestamp": time.time(),
        "trace_id": trace_id or str(uuid.uuid4()),
        "user_id": user_id,
        "action": action,
        "status": status,
        "details": details
    }
    db.log_audit(entry)
    print(f"[AUDIT] {entry}") # Print to console for workshop visibility
