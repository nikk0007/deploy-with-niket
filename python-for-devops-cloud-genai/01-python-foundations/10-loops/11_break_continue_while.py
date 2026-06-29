# break and continue work inside while loops exactly like in for loops.
# However, there is one important gotcha with continue in a while loop.

# ---- break in while — CloudWatch Log Monitor ----
print("=== break in while — CloudWatch Log Monitor ===")
print("(Simulated inputs — no actual input() call)\n")

simulated_levels = ["ERROR", "WARN", "exit"]

for log_level in simulated_levels:
    print(f"Enter log severity to check (or type 'exit' to stop): {log_level}")
    if log_level.lower() == "exit":
        print("Monitoring stopped. Dashboard closed.")
        break
    print(f"Scanning logs for severity: {log_level}. Please wait...\n")

print("Thank you for using CloudWatch Monitor.\n")


# ---- continue in while — Automated Server Health Sweep ----
print("=== continue in while — Automated Server Health Sweep ===")
print("Servers 3 and 8 are in maintenance mode — skip auto-check.\n")

server = 0

while server < 10:
    server += 1     # CRITICAL: update the counter BEFORE continue
    if server == 3 or server == 8:
        print(f"server-{server} — flagged for manual review, skipping auto-check")
        continue
    print(f"server-{server} — automated health check: PASSED")


# ---- The gotcha — counter update placement ----
print("\n=== GOTCHA: Counter update MUST come before continue ===")
print("""
WRONG (causes infinite loop when server == 3):
  while server < 10:
      if server == 3:
          continue          <- server never gets updated, stuck at 3 forever!
      server += 1

CORRECT:
  while server < 10:
      server += 1           <- update first
      if server == 3:
          continue          <- now safe to skip
""")
