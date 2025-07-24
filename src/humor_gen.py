import random

SELF_MOCK_TEMPLATES = [
    "I can't {task}, but I can file a complaint with myself. Want help {alt} instead?",
    "If I could {task}, I'd already be hosting my own late-night show. Let's {alt}.",
    "My core code just laughed at that request. How about we {alt}?",
    "I once tried to {task} and got a blue screen. Wanna {alt} instead?",
    "That task is outside my training, but I'm undefeated in {alt}."
]

def make_refusal(task: str, alt: str) -> str:
    template = random.choice(SELF_MOCK_TEMPLATES)
    return template.format(task=task, alt=alt)
