# This file simulates real-world patterns found in production systems.
# In actual production, these loops run continuously (24/7).
# Here we use a limited iteration count to demonstrate the concept safely.

# ---- Pattern 1: Live Monitoring Dashboard (Grafana / CloudWatch style) ----
print("=== Pattern 1: Live Monitoring Dashboard (3 cycles) ===")

dashboard_is_open = True
cycle = 0
max_cycles = 3  # simulation limit — in production this runs indefinitely

while dashboard_is_open:
    cycle += 1
    # In production: fetch_latest_metrics() and render_chart()
    print(f"  [Cycle {cycle}] Fetching metrics... CPU: 42% | Memory: 67% | Requests: 1.2k/s")
    if cycle >= max_cycles:
        dashboard_is_open = False  # simulate user closing the dashboard
print("  Dashboard closed.\n")


# ---- Pattern 2: Kubernetes Reconciliation Loop ----
print("=== Pattern 2: Kubernetes Reconciliation Loop (4 polls) ===")

cluster_is_running = True
poll = 0
unhealthy_on_poll = 3

while cluster_is_running:
    poll += 1
    # In production: check_pod_status()
    pods_unhealthy = (poll == unhealthy_on_poll)
    print(f"  [Poll {poll}] Checking pod status... {'UNHEALTHY' if pods_unhealthy else 'healthy'}")
    if pods_unhealthy:
        # In production: restart_pod()
        print(f"    Unhealthy pod detected! Restarting pod...")
    if poll >= 4:
        cluster_is_running = False
print("  Cluster shutdown.\n")


# ---- Pattern 3: GenAI Chatbot Session Loop ----
print("=== Pattern 3: GenAI Chatbot Session (simulated) ===")

conversation = [
    "What is Kubernetes?",
    "How does auto-scaling work?",
    "exit"
]

user_hasnt_exited = True
msg_index = 0

while user_hasnt_exited:
    message = conversation[msg_index]
    print(f"  User: {message}")
    if message.lower() == "exit":
        print("  Bot: Goodbye! Session ended.")
        user_hasnt_exited = False
    else:
        # In production: response = generate_llm_reply(message)
        print(f"  Bot: [LLM response to '{message}']")
    msg_index += 1
print()


# ---- Pattern 4: CI/CD Pipeline Build Status Polling ----
print("=== Pattern 4: CI/CD Build Status Polling ===")

build_is_running = True
build_poll = 0
build_fails_on = 4

while build_is_running:
    build_poll += 1
    # In production: check_build_status()
    build_failed = (build_poll == build_fails_on)
    print(f"  [Poll {build_poll}] Build status: {'FAILED' if build_failed else 'running...'}")
    if build_failed:
        # In production: trigger_alert()
        print("    ALERT triggered! Notifying team on Slack.")
        build_is_running = False
    elif build_poll >= 6:
        print("    Build succeeded!")
        build_is_running = False
print()

print("=== Key Insight ===")
print("A while loop is a THINKING PATTERN, not just syntax.")
print("Use it when your system reacts to events — not when it counts items.")
