# ---- pass — The Placeholder ----
# Use pass when you want to write a skeleton first and fill in logic later.
# It does nothing, but prevents a syntax error on an empty block.
print("=== pass — Placeholder (no output) ===")
for i in range(5):
    pass  # logic will go here later
print("Loop with 'pass' completed — nothing happened inside.\n")


# ---- continue — Skip the current iteration ----
print("=== continue — Skip even numbers ===")
for n in range(1, 11):
    if n % 2 == 0:
        continue        # skip even numbers, move to next iteration
    print(f"Odd number: {n}")


# ---- break — Exit the loop immediately ----
print("\n=== break — Stop at first match ===")
targets = [10, 25, 30, 50, 75]
threshold = 40

for value in targets:
    if value >= threshold:
        print(f"Threshold crossed at value: {value}. Stopping.")
        break           # exit the loop right now
    print(f"Value {value} is below threshold.")


# ---- pass inside an if block (not a loop) ----
# Also commonly used when you want one branch of an if to do nothing yet.
print("\n=== pass in if block — Common pattern ===")
status = "warning"
if status == "critical":
    print("ALERT: Critical status!")
elif status == "warning":
    pass    # no action for warnings yet — logic to be added later
else:
    print("All clear.")
print("Script continues after pass...\n")
