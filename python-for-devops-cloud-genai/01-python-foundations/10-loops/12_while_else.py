# Rule: The else block runs when the loop condition naturally becomes False.
#       If the loop exits via break — the else block is SKIPPED entirely.

# ---- Case 1: Transaction found — break fires, else is skipped ----
print("=== Case 1: Transaction FOUND (break fires, else skipped) ===")

batch = 1
target_transaction_id = "TXN-48291"

while batch <= 8:
    print(f"Scanning log batch {batch}...")
    if batch == 5:   # simulation: transaction is found in batch 5
        print(f"Transaction {target_transaction_id} found in batch {batch}. Deployment verified.")
        break
    batch += 1
else:
    print(f"Transaction {target_transaction_id} NOT found. Triggering rollback alert.")

print()

# ---- Case 2: Transaction NOT found — loop ends naturally, else runs ----
print("=== Case 2: Transaction NOT FOUND (else fires) ===")

batch = 1
target_transaction_id = "TXN-99999"   # this one does not exist in any batch

while batch <= 8:
    print(f"Scanning log batch {batch}...")
    if batch == -1:   # condition is never true — break never fires
        break
    batch += 1
else:
    print(f"Transaction {target_transaction_id} NOT found in any batch. Triggering rollback alert.")

print()

# ---- Case 3: API retry with while-else ----
print("=== Case 3: API Retry — succeed or exhaust all attempts ===")

max_retries = 3
attempt = 1
api_success_on = 2   # change to 99 to simulate total failure

while attempt <= max_retries:
    print(f"Attempt {attempt}: Calling API...")
    if attempt == api_success_on:
        print(f"  API call succeeded on attempt {attempt}.")
        break
    print(f"  API call failed. Retrying...")
    attempt += 1
else:
    print("  All retry attempts exhausted. Alerting on-call team.")

print()

# ---- Summary ----
print("=== while-else Use Cases ===")
print("1. Search loop  — was the item found or not?")
print("2. Retry logic  — did it succeed or did all attempts run out?")
print("3. Input validation — was valid input received or did the user give up?")
print("\nWithout else — you need an extra 'found = False' flag variable.")
print("With while-else — clean code, no extra variables needed.")
