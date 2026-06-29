# ---- Example 1: EC2 Instance Batch Restart ----
print("=== EC2 Instance Batch Restart (10 instances) ===")
for instance_id in range(1, 11):
    print(f"Restarting EC2 instance #{instance_id} — please wait...")

print()

# ---- Example 2: CI/CD Pipeline Stages ----
print("=== CI/CD Pipeline — 7 Stages ===")
for stage in range(1, 8):
    print(f"Pipeline stage #{stage} executing — build server is live!")

print()

# ---- Example 3: The variable name does not change the behaviour ----
# You can name the loop variable anything — x, i, stage, anything.
# The name is only for readability; Python does not care what you call it.
print("=== Variable name does not change behaviour ===")
for x in range(1, 4):
    print(f"x = {x}")

for i in range(1, 4):
    print(f"i = {i}")

for anything in range(1, 4):
    print(f"anything = {anything}")

# All three loops produce identical output.
