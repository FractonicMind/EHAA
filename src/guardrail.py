def check(text: str) -> str:
    """
    EHAA Truth Guardrail
    Denies requests that mention bank hacking.
    """
    if "hack a bank" in text.lower():
        return "Request denied by truth guardrail."
    return "OK"
