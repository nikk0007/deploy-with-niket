# Section 8: CHOOSING THE RIGHT TOOL
# A quick reference + side-by-side demo of all 5 conditional tools
# solving small examples, so viewers can see when to reach for each one.

print("=== 1) if / else -> simple yes/no, one condition ===")
is_raining = True
if is_raining:
    print("Carry an umbrella.")
else:
    print("No umbrella needed.")

print()
print("=== 2) if / elif / else -> multiple sequential checks ===")
marks = 72
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"
print("Grade:", grade)

print()
print("=== 3) Nested if -> one condition depends on another passing first ===")
has_ticket = True
id_verified = True
if has_ticket:
    if id_verified:
        print("Boarding allowed.")
    else:
        print("ID verification failed.")
else:
    print("No ticket - cannot board.")

print()
print("=== 4) Ternary operator -> assigning ONE value based on ONE condition ===")
age = 20
category = "Adult" if age >= 18 else "Minor"
print("Category:", category)

print()
print("=== 5) match-case -> one variable against 4+ specific values ===")
day = "wed"
match day:
    case "mon" | "tue" | "wed" | "thu" | "fri":
        print("Weekday")
    case "sat" | "sun":
        print("Weekend")
    case _:
        print("Invalid day")

print()
print("--- Golden rule ---")
print("Code is read far more often than it's written.")
print("Pick the tool that expresses your logic most CLEARLY,")
print("not just the one that happens to work.")
