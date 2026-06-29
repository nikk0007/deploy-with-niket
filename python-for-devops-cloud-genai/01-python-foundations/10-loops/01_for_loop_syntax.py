# Basic for loop structure:
#
#   for variable in sequence:
#       # code to execute
#
# - for           → keyword that starts the loop
# - variable      → temporary name; its value changes every iteration
# - in            → connects the variable to the sequence
# - sequence      → what you want to loop over (range, list, string, etc.)
# - :             → colon is required — don't forget it
# - indented block → code inside the loop (use tab or 4 spaces)

services = ["auth-service", "payment-service", "notification-service"]

# ---- Example 1: Simple list loop ----
print("=== Health Check for All Services ===")
for service in services:
    print(f"Health check passed for {service}")

# ---- Example 2: String is also a sequence ----
print("\n=== Characters in 'devops' ===")
for char in "devops":
    print(char)

# ---- Example 3: What is INSIDE vs OUTSIDE the loop ----
print("\n=== Inside vs Outside Indentation ===")
for service in services:
    # This runs on every iteration (indented — inside the loop)
    print(f"  [INSIDE loop]  Checking: {service}")

# This runs only ONCE (no indent — outside the loop, after it ends)
print("[OUTSIDE loop] All services checked.\n")
