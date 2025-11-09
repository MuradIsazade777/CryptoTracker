def is_valid_text(text: str) -> bool:
    return bool(text and len(text.strip()) > 0)

def is_valid_key(key: str) -> bool:
    return len(key) >= 16
