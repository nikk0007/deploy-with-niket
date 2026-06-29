# Story: A traffic spike hits production. The Auto Scaling Group
# needs to spin up 3 new instances to reach the target capacity.

print("=== Auto Scaling Group — Capacity Ramp-Up ===")

instances_needed = 3
instances_running = 0

while instances_running < instances_needed:
    instances_running += 1
    print(f"Spinning up instance #{instances_running}...")

print(f"Target capacity reached ({instances_needed} instances). Auto Scaling Group stable.\n")

# ---- Step-by-step trace of each iteration ----
print("=== Step-by-step trace ===")
instances_needed = 3
instances_running = 0

iteration = 0
while instances_running < instances_needed:
    iteration += 1
    print(f"Check {iteration}: instances_running={instances_running} < {instances_needed}? "
          f"{'True — running block' if instances_running < instances_needed else 'False — stopping'}")
    instances_running += 1
    print(f"  → instances_running updated to {instances_running}")

print(f"Final check: {instances_running} < {instances_needed}? False → loop exits.\n")

# ---- What happens if you forget the counter update? ----
# DO NOT run this — it is an infinite loop (shown for educational purposes only):
#
# instances_running = 0
# while instances_running < instances_needed:
#     print("This will print FOREVER — counter never updates!")
#     # instances_running += 1  ← missing line causes the infinite loop
