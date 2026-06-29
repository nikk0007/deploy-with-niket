# break: the moment it is hit — exit the loop immediately.
# continue keeps the loop alive and skips one round.
# break ends the loop right there, right now.

# ---- Example 1: Cloud Cost Anomaly Detection ----
print("=== Cloud Cost Anomaly Detector ===")

daily_costs = [120, 145, 132, 98000, 110, 128]
COST_ALERT_THRESHOLD = 50000

for cost in daily_costs:
    if cost >= COST_ALERT_THRESHOLD:
        print(f"ALERT: Unusual cloud spend of Rs.{cost} detected. Pausing auto-scaling.")
        break   # stop immediately — do NOT process remaining entries
    print(f"Daily cost Rs.{cost} — within normal range.")

print("\n(Rs.110 and Rs.128 were NEVER processed — break fired first)\n")

# ---- Example 2: The intro bug — what happens without break ----
print("=== What happens WITHOUT break (the intro bug) ===")

servers = ["server-1", "server-2", "server-3-DOWN", "server-4", "server-5"]

print("WITHOUT break — deployment continues past the down server (bug):")
for server in servers:
    if "DOWN" in server:
        print(f"  ALERT: {server} is down! (but the loop keeps going...)")
    else:
        print(f"  {server} — health check OK, deploying...")

print()
print("WITH break — deployment stops immediately (correct behaviour):")
for server in servers:
    if "DOWN" in server:
        print(f"  ALERT: {server} is down! Halting deployment NOW.")
        break
    print(f"  {server} — health check OK, deploying...")

print()

# ---- Example 3: Stop searching once you find the first match ----
print("=== Search: Find First Available GPU Instance ===")

instances = [
    ("t3.medium", "available"),
    ("g4dn.xlarge", "out_of_stock"),
    ("p3.2xlarge", "available"),
    ("p4d.24xlarge", "available"),
]

target = "p3.2xlarge"

for instance_type, status in instances:
    if instance_type == target and status == "available":
        print(f"Found: {instance_type} is available. Launching now.")
        break   # found what we need — no point checking further
    print(f"  Checking {instance_type}... not a match or not available.")

print("""
Mental Model:
  break = an airport security scanner.
  Bags are coming down the conveyor belt.
  A prohibited item is detected — everything stops. Full stop. Investigation begins.
  That is exactly what break does in code.
""")
