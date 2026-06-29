# DEMO 9 — The 80/20 Rule
# The 3 comprehension patterns you'll use in 90% of real DevOps/Cloud/GenAI code

# ── Pattern 1: TRANSFORM ──
# Real scenario: normalize service names received from a config file
service_names = ["auth service", "payment service", "notification service"]
normalized = [name.replace(" ", "-").lower() for name in service_names]
print(normalized)
# Output: ['auth-service', 'payment-service', 'notification-service']


# ── Pattern 2: FILTER ──
# Real scenario: find pods that crossed the CPU threshold
cpu_usage = [45, 78, 92, 30, 88]
overloaded = [usage for usage in cpu_usage if usage > 75]
print(overloaded)
# Output: [78, 92, 88]


# ── Pattern 3: DICT BUILD ──
# Real scenario: build a quick lookup table of model name -> name length
# (in practice you'd map to something like max_token_limit, cost_per_token, etc.)
model_names = ["gpt-4", "claude-3", "gemini-pro"]
model_lookup = {name: len(name) for name in model_names}
print(model_lookup)
# Output: {'gpt-4': 5, 'claude-3': 8, 'gemini-pro': 10}

# Master these three patterns — Transform, Filter, Dict Build —
# and you can read and write almost any comprehension you'll encounter
# in real production Python code.
