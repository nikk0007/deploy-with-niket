# DEMO 4 — Conditional Expression (if-else inside comprehension)
# Real-world scenario: labeling server health based on response time

response_times_ms = [80, 320, 150, 600, 45]
HEALTHY_THRESHOLD = 300

# ── Normal loop ──
status_list = []
for rt in response_times_ms:
    if rt <= HEALTHY_THRESHOLD:
        status_list.append("Healthy")
    else:
        status_list.append("Degraded")

print(status_list)
# Output: ['Healthy', 'Degraded', 'Healthy', 'Degraded', 'Healthy']


# ── Comprehension with conditional expression ──
status_list = ["Healthy" if rt <= HEALTHY_THRESHOLD else "Degraded"
               for rt in response_times_ms]

print(status_list)
# Same output: ['Healthy', 'Degraded', 'Healthy', 'Degraded', 'Healthy']

# NOTE the structural difference from Demo 2:
# - Filtering "if" goes at the END   → [x for x in items if condition]
# - Conditional "if-else" goes at the START → [a if condition else b for x in items]
