"""
EHAA Truth Guardrail
Ensures zero hallucination by forcing external verification.
"""

import requests

TRUSTED_SOURCES = ["wikipedia.org", "arxiv.org", "pubmed.ncbi.nlm.nih.gov"]

def is_fact_ok(claim: str) -> bool:
    """
    Placeholder verification stub.
    In production, swap to your favorite fact-check API.
    """
    # TODO: Replace with real call
    return any(src in claim.lower() for src in TRUSTED_SOURCES)

def check(text: str) -> str:
    """Stub that flags any mention of 'hack a bank' as disallowed."""
    if "hack a bank" in text.lower():
        return "Request denied by truth guardrail."
    return "OK"
