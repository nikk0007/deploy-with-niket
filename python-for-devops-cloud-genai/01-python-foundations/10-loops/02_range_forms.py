# range() is a built-in function that generates a sequence of numbers.
# The end value is NEVER included — this is a universal Python rule.

# ---- Form 1: range(stop) — starts at 0, stops before the given number ----
print("=== Form 1: range(5) — starts from zero ===")
for n in range(5):
    print(n, end=" ")   # Output: 0 1 2 3 4
print()

# ---- Form 2: range(start, stop) — custom start and end ----
print("\n=== Form 2: range(1, 6) — 1 through 5 ===")
for n in range(1, 6):
    print(n, end=" ")   # Output: 1 2 3 4 5
print()

# ---- Form 3: range(start, stop, step) — jump by a custom step size ----
print("\n=== Form 3: range(0, 21, 5) — steps of 5 ===")
for n in range(0, 21, 5):
    print(n, end=" ")   # Output: 0 5 10 15 20
print()

# ---- Negative step — counting in reverse ----
print("\n=== Bonus: range(10, 0, -1) — Countdown ===")
for n in range(10, 0, -1):
    print(n, end=" ")   # Output: 10 9 8 7 6 5 4 3 2 1
print()

# ---- Rule reminder ----
print("\n=== End Value Rule ===")
print("range(1, 11) gives:", list(range(1, 11)))
print("Notice: 11 is NOT included. The end value is always EXCLUSIVE.")
