# continue has one job:
# Skip the current iteration and move on to the next one.
# The loop does NOT stop — only that one round is skipped.

# ---- Example 1: Cloud Region Filter — skip INVALID entries ----
print("=== Cloud Region Filter — Skip INVALID Entries ===")

regions = ["ap-south-1", "INVALID", "us-east-1", "INVALID", "eu-west-1", "INVALID"]

for region in regions:
    if region == "INVALID":
        continue       # skip this entry, move to the next region
    print(f"Deployment scheduled for region: {region}")

print()

# ---- Example 2: Skip degraded services in a health report ----
print("=== Microservice Health Report — Skip Degraded Services ===")

services = [
    ("auth-service", "healthy"),
    ("payment-service", "degraded"),
    ("notification-service", "healthy"),
    ("search-service", "degraded"),
    ("api-gateway", "healthy"),
]

print("Processing only HEALTHY services:")
for service, status in services:
    if status == "degraded":
        print(f"  [SKIPPED] {service} is degraded — manual review needed")
        continue
    print(f"  [OK] {service} — processing metrics")

print()

# ---- Example 3: Skip invalid token counts in a log batch ----
print("=== Log Batch Size Filter — Skip Zero or Negative Counts ===")

log_batches = [150, -1, 340, 0, 220, -1, 180]

total = 0
skipped = 0

for size in log_batches:
    if size <= 0:
        skipped += 1
        continue    # invalid entry — skip it
    total += size
    print(f"  Batch size {size} added to total.")

print(f"\nTotal valid log entries: {total}")
print(f"Skipped invalid entries: {skipped}")

print("""
Mental Model:
  continue = an automated linter skipping a commented-out line.
  The file scan does not stop — only that one line is skipped, then it moves on.
""")
