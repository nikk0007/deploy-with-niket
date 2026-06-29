# for-else removes the need for an extra "found" flag variable.
# Both approaches produce the same result — for-else is cleaner and more Pythonic.

available_instances = [
    ("t3.medium", "available"),
    ("g4dn.xlarge", "out_of_stock"),
    ("p3.2xlarge", "out_of_stock"),
]
target_gpu = "p3.2xlarge"

# ---- Old approach: flag variable ----
print("=== Old Approach — Flag Variable ===")

found = False   # extra variable required

for instance_type, status in available_instances:
    if instance_type == target_gpu and status == "available":
        print(f"GPU instance found: {instance_type}")
        found = True
        break

if not found:   # extra if statement required
    print("No available capacity. Sending alert to on-call SRE.")

print()

# ---- New approach: for-else ----
print("=== New Approach — for-else (Pythonic) ===")

for instance_type, status in available_instances:
    if instance_type == target_gpu and status == "available":
        print(f"GPU instance found: {instance_type}")
        break
else:
    print("No available capacity. Sending alert to on-call SRE.")

print()

# ---- Side-by-side comparison ----
print("=== Side-by-Side Comparison ===")
print("""
FLAG VARIABLE (old):                  FOR-ELSE (Pythonic):
──────────────────────────────────    ───────────────────────────────────
found = False                         for item in collection:
                                          if condition:
for item in collection:                       break
    if condition:                 →   else:
        found = True                      # not-found action
        break

if not found:
    # not-found action

Differences:
  - Flag variable: 1 extra variable + 1 extra if check after the loop
  - for-else:      No extra variable, no extra if
  - for-else:      Shorter, cleaner, harder to accidentally forget
  - for-else:      Shows the interviewer that you know idiomatic Python
""")

# ---- One more real example: package dependency check ----
print("=== Real Example: Required Package Check ===\n")

installed_packages = ["numpy", "pandas", "requests", "boto3"]
required = "torch"

print(f"Checking if '{required}' is installed...")

for pkg in installed_packages:
    if pkg == required:
        print(f"  '{required}' found! Good to go.")
        break
else:
    print(f"  '{required}' NOT found. Run: pip install {required}")
