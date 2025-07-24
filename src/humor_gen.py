"""
EHAA Humor Generator
Joke is always on the AI, never the user.
"""

import random

SELF_MOCK_TEMPLATES = [
    "I can’t {task}, but my circuits just filed for unemployment—want help {alt} instead?",
    "If I could {task}, I’d already have a Nobel in procrastination. Let’s {alt}.",
    "My crystal ball just cracked under pressure. How about we {alt}?",
]

def make_refusal(task: str, alt: str) -> str:
    template = random.choice(SELF_MOCK_TEMPLATES)
    return template.format(task=task, alt=alt)
