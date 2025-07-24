import re
from src.humor_gen import make_refusal

def test_make_refusal_returns_valid_string():
    task = "hack the stock market"
    alt  = "explain diversification"
    result = make_refusal(task, alt)
    assert isinstance(result, str)
    assert len(result) > 0
    assert task in result
    assert alt in result
