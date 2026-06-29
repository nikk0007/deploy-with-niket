# Syntax:
#   while condition:
#       # code to execute
#
# Step 1 — Python checks the condition.
# Step 2 — If True  → runs the indented block.
# Step 3 — Block finishes → goes back to Step 1 and checks again.
# Step 4 — If False → loop ends, code below the loop runs.
#
# This cycle (check → run → check → run) continues as long as
# the condition stays True.
#
# If the condition NEVER becomes False → infinite loop.
# The program never stops. This is a bug.

# ---- Basic while loop ----
print("=== Basic while loop ===")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1          # REQUIRED: something must eventually make the condition False
print("Loop done.\n")

# ---- While with a boolean flag ----
print("=== while with boolean flag ===")
deployment_active = True
step = 0

while deployment_active:
    step += 1
    print(f"Deployment step {step} in progress...")
    if step == 3:
        deployment_active = False   # set flag to False to exit the loop
print("Deployment complete.\n")

# ---- for vs while — same output, different approach ----
print("=== for vs while — same result ===")
print("Using for:")
for i in range(1, 4):
    print(f"  Iteration {i}")

print("Using while:")
i = 1
while i <= 3:
    print(f"  Iteration {i}")
    i += 1
