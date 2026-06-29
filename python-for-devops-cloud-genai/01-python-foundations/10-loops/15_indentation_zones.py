# Understanding which zone code lives in determines WHEN it runs.
#
# Zone 1 — inside an if block:          runs only when that condition is True
# Zone 2 — inside the loop, outside if: runs on every iteration
# Zone 3 — after the loop:              runs exactly once, after the loop ends

# ---- Zone diagram ----
print("""
ZONE DIAGRAM:
─────────────────────────────────────
for entry in log_entries:         <- loop header
    if entry == "SKIP":           |
        continue                  |  <- ZONE 1 (inside the if block)
    if entry == "STOP":           |
        break                     |  <- ZONE 1 (inside the if block)
    print(entry)                  <- ZONE 2 (inside loop, outside any if)
                                     (runs on every iteration)
print("Loop finished")            <- ZONE 3 (outside the loop, runs once)
─────────────────────────────────────
""")


# ---- Live experiment — predict the output before you run! ----
print("=== Live Experiment: Predict the Output First! ===\n")
print("Log entries: ['INFO: server started', 'SKIP', 'INFO: health check passed', 'STOP', 'INFO: this should not print']")
print("Rules: 'SKIP' triggers continue (skip it), 'STOP' triggers break (stop the loop)")
print("\nPredict what will print — then check the actual output below.\n")

log_entries = [
    "INFO: server started",
    "SKIP",
    "INFO: health check passed",
    "STOP",
    "INFO: this should not print"
]

for entry in log_entries:
    if entry == "SKIP":
        continue         # Zone 1: skip this iteration
    if entry == "STOP":
        break            # Zone 1: stop the loop entirely
    print(f"Processing: {entry}")   # Zone 2: runs each iteration (unless skipped or stopped)

print("Log processing complete.")   # Zone 3: runs once after the loop


# ---- Explanation ----
print("""
Explanation:
1. "INFO: server started"       no skip or stop  -> Zone 2 prints it         [printed]
2. "SKIP"                       continue fires   -> Zone 2 is skipped        [skipped]
3. "INFO: health check passed"  no skip or stop  -> Zone 2 prints it         [printed]
4. "STOP"                       break fires      -> loop ends immediately    [stopped]
5. "INFO: this should not..."   never reached    -> break already fired      [not reached]
-> Zone 3 runs once after the loop ends.
""")
