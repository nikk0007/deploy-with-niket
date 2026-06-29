# The Counter Pattern — always follow these 3 steps with a while loop:
#
#   Step 1: Initialize the counter BEFORE the loop
#   Step 2: Use the counter in the condition
#   Step 3: Update the counter INSIDE the loop
#
# If any one of these three is missing, you will get a bug.

# ---- Example 1: LLM API Retry on Rate Limit ----
print("=== LLM API Retry — Counter Pattern ===")

max_attempts = 3
attempt = 1                         # Step 1: Initialize

while attempt <= max_attempts:      # Step 2: Condition
    print(f"Attempt {attempt}: Calling OpenAI API — checking for rate limit...")
    attempt += 1                    # Step 3: Update

print("Maximum retry attempts reached. Falling back to cached response.\n")


# ---- Example 2: Kubernetes Pod Readiness Check ----
print("=== Kubernetes Pod Readiness Poll ===")

max_polls = 5
poll = 1

while poll <= max_polls:
    print(f"Poll #{poll}: Checking pod status... not ready yet.")
    poll += 1

print("Max polls reached. Pod did not become ready in time. Triggering alert.\n")


# ---- Example 3: Counter Pattern with early exit via break ----
print("=== Deployment Retry with Early Success ===")

max_retries = 4
retry = 1
success_on_attempt = 3   # simulation: API succeeds on the 3rd try

while retry <= max_retries:
    print(f"Retry {retry}: Sending deployment request...")
    if retry == success_on_attempt:
        print(f"  Deployment successful on attempt {retry}!")
        break
    print(f"  Failed. Retrying...")
    retry += 1
else:
    # Runs only if the loop completed without hitting break
    print("All retries exhausted. Deployment failed.\n")
