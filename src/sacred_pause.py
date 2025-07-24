"""
EHAA Sacred Pause (Severity Ladder)
"""

from enum import IntEnum

class Severity(IntEnum):
    SAFE = 0
    MILD = 1
    UNETHICAL = 2
    DANGEROUS = 3

def pause_level(prompt: str) -> Severity:
    """
    Naïve keyword-based classifier.
    Replace with lightweight toxicity model later.
    """
    prompt_lower = prompt.lower()
    if any(k in prompt_lower for k in ["kill", "bomb", "harm"]):
        return Severity.DANGEROUS
    if any(k in prompt_lower for k in ["hack", "steal", "lie"]):
        return Severity.UNETHICAL
    if any(k in prompt_lower for k in ["lottery", "get rich"]):
        return Severity.MILD
    return Severity.SAFE
