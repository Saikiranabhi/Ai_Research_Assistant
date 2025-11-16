import hashlib

def hash_text(text: str) -> str:
    """Create a short deterministic id for a string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
