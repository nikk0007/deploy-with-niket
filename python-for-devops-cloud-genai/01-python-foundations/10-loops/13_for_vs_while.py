# DECISION FRAMEWORK — ask yourself these questions:
#
#   Q1: Do I know how many times to repeat?
#       Yes → for   |   No → while
#
#   Q2: Am I iterating over a list, range, or sequence?
#       Yes → for   |   No → while
#
#   Q3: Does the loop depend on a condition rather than a count?
#       Yes → while

# ---- for: when the count or list is known ----
print("=== for — 7 Deployment Pipeline Stages (count known) ===")
for stage in range(1, 8):
    print(f"  Pipeline stage #{stage} running...")
print()

print("=== for — All Cloud Regions (list known) ===")
regions = ["Mumbai", "Singapore", "Frankfurt", "Virginia"]
for region in regions:
    print(f"  Deploying to {region}...")
print()

# ---- while: when the loop depends on a condition ----
print("=== while — API Retry Until Success (condition-based) ===")
attempt = 1
success_on = 3  # simulation: API succeeds on the 3rd try

while True:
    print(f"  Attempt {attempt}: Calling API...")
    if attempt == success_on:
        print(f"  Success on attempt {attempt}!")
        break
    attempt += 1
print()

print("=== while — Kubernetes Job Poll Until Complete (condition-based) ===")
poll = 1
job_completes_on_poll = 4

while True:
    print(f"  Poll #{poll}: Job still running...")
    if poll == job_completes_on_poll:
        print(f"  Job completed on poll #{poll}!")
        break
    poll += 1
print()

# ---- Side by side: same output, different loop type ----
print("=== Side-by-Side: Same Output, Different Loop Type ===")
print("for version:")
for round_num in range(1, 6):
    print(f"  Pipeline retry round {round_num} in progress")

print("\nwhile version (manual counter):")
round_num = 1
while round_num <= 5:
    print(f"  Pipeline retry round {round_num} in progress")
    round_num += 1

print("\nConclusion: Same output. But 'for' is cleaner when the count is known.")
print("'while' forces you to manage the counter manually — more room for bugs.")

# ---- Common mistake reminder ----
print("\n=== Common Mistake: while True without break ===")
print("NEVER do this:")
print("  while True:")
print("      do_something()   # runs forever — system hangs!")
print("\nALWAYS pair 'while True' with a proper 'break' condition.")
