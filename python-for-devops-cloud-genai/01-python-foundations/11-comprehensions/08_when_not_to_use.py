# DEMO 8 — When NOT to Use Comprehensions
# Scenario: filtering GenAI API call logs that exceeded both cost AND latency limits

api_calls = [
    {"model": "gpt-4", "cost": 0.42, "latency_ms": 1800},
    {"model": "claude-3", "cost": 0.18, "latency_ms": 900},
    {"model": "gpt-4", "cost": 0.55, "latency_ms": 2400},
]

COST_LIMIT = 0.30
LATENCY_LIMIT = 1500


def exceeds_cost(call):
    return call["cost"] > COST_LIMIT


def exceeds_latency(call):
    return call["latency_ms"] > LATENCY_LIMIT


# ── BAD: cramming too much logic into one comprehension ──
# This technically works, but it is hard to read at a glance.
flagged_calls_bad = [
    call
    for call in api_calls
    if exceeds_cost(call)
    and exceeds_latency(call)
]

print(flagged_calls_bad)


# ── GOOD: use a normal for loop when logic gets complex ──
flagged_calls_good = []
for call in api_calls:
    if exceeds_cost(call) and exceeds_latency(call):
        flagged_calls_good.append(call)

print(flagged_calls_good)

# Both give the same output. But the for loop version is easier to debug,
# easier to add a print() inside for troubleshooting, and easier for a
# teammate to read during a code review.

# RULE OF THUMB:
# If you have to pause and re-read a comprehension to understand it —
# it's time to switch back to a normal for loop.
