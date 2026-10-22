# Build: 4ee1942629a8cf38311c7e8aa2b3799b

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
