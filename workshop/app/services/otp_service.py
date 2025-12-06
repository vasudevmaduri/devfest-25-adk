"""
Mock OTP Service.
"""
import random

# Store active OTPs in memory: {user_id: code}
_active_otps = {}

def send_otp(user_id: str) -> str:
    """Generates and 'sends' an OTP (prints to console)."""
    code = f"{random.randint(100000, 999999)}"
    _active_otps[user_id] = code
    print(f"\n[OTP SERVICE] Sending code {code} to user {user_id}\n")
    return code

def verify_otp(user_id: str, code: str) -> bool:
    """Verifies the OTP."""
    if user_id in _active_otps and _active_otps[user_id] == code:
        del _active_otps[user_id]
        return True
    return False
