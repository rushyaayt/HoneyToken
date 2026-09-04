import secrets
import string
from typing import Dict

def generate_api_key(prefix: str = "ht_", length: int = 32) -> str:
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return f"{prefix}{token}"


def fake_user(username_prefix: str = "user_") -> Dict[str, str]:
    uid = secrets.token_hex(8)
    username = f"{username_prefix}{uid[:6]}"
    email = f"{username}@example.com"
    return {"id": uid, "username": username, "email": email}


def fake_db_row(table: str = "customers") -> Dict[str, str]:
    return {"table": table, "id": secrets.token_hex(6), "note": "honeytoken row"}
