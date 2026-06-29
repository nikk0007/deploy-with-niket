# Rule:
#   else runs when the loop completes NATURALLY (break never fired).
#   If break fired — else is SKIPPED entirely. No exceptions.

# ---- Example 1: GPU Instance Availability Search ----
print("=== GPU Instance Search — p3.2xlarge ===\n")

available_instances = [
    ("t3.medium", "available"),
    ("g4dn.xlarge", "out_of_stock"),
    ("p3.2xlarge", "out_of_stock"),
]
target_gpu = "p3.2xlarge"

for instance_type, status in available_instances:
    if instance_type == target_gpu and status == "available":
        print(f"GPU instance found: {instance_type}. Launching now.")
        break
else:
    # p3.2xlarge exists but is out_of_stock — condition never fully matched — no break
    print(f"No available capacity for {target_gpu}. Sending alert to on-call SRE.")

print()

# ---- Example 2: Pre-Deployment Server Health Gate ----
print("=== Pre-Deployment Health Gate ===\n")

servers = ["server-mumbai", "server-delhi", "server-hyderabad"]
down_servers = ["server-delhi"]

print(f"Down servers: {down_servers}")
print("Checking all servers before deployment...\n")

for server in servers:
    if server in down_servers:
        print(f"CRITICAL: {server} is down. Halting deployment.")
        break
else:
    print("All servers healthy. Deployment approved. Going live.")

print()

# ---- Same check with no servers down — else fires ----
print("=== Same check — no servers down ===\n")
down_servers = []   # all servers are healthy

for server in servers:
    if server in down_servers:
        print(f"CRITICAL: {server} is down. Halting deployment.")
        break
else:
    print("All servers healthy. Deployment approved. Going live.")

print()

# ---- Rule summary ----
print("=== for-else Rule ===")
print("break fired       → else is SKIPPED")
print("break NOT fired   → else RUNS (loop completed fully)")
print("\nMental model: 'else' = what to do when the search came up empty.")
