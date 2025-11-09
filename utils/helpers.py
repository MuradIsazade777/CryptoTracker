from datetime import datetime

def current_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_wallet_entry(name: str, encrypted_key: str) -> str:
    return f"{current_timestamp()} | {name}: {encrypted_key}"
