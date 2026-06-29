# ---- THE BUG — an accidental infinite loop ----
# DO NOT run this block (commented out for safety):
#
# count = 1
# while count <= 5:
#     print(f"Checking log batch: {count}")
#     # count += 1  ← MISSING! This will run FOREVER.
#     # Press Ctrl+C to stop if you accidentally run it.

print("=== Bug Example (safe version — finite) ===")
print("If 'count += 1' were missing, this would run forever.")
print("Below is the CORRECT version:\n")

count = 1
while count <= 5:
    print(f"Checking log batch: {count}")
    count += 1      # This one line prevents an infinite loop
print("Done.\n")


# ---- THE PATTERN — intentional while True with break ----
# 'while True' is valid and professional — as long as you pair it with break.

print("=== Valid Pattern: while True with break ===")
print("(Using simulated input — no actual input() call)\n")

correct_api_key = "sk-prod-92xZ"
test_inputs = ["wrong-key", "another-wrong", "sk-prod-92xZ"]   # simulated user inputs

for simulated_input in test_inputs:
    print(f"Enter deployment API key: {simulated_input}")
    if simulated_input == correct_api_key:
        print("API key verified. Proceeding with deployment...")
        break
    print("Incorrect API key. Please try again.\n")


# ---- Interactive version (uncomment to run) ----
# while True:
#     entered_key = input("Enter deployment API key: ")
#     if entered_key == correct_api_key:
#         print("API key verified. Proceeding with deployment...")
#         break
#     print("Incorrect API key. Please try again.")


print("\n=== Rule Summary ===")
print("while True WITHOUT break  → BUG   (infinite loop, system hangs)")
print("while True WITH proper break → PROFESSIONAL PATTERN")
