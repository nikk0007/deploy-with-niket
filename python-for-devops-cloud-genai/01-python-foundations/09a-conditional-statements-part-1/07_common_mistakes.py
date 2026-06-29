# Section 8: Common Mistakes (Beginner Errors)
# Each mistake below is shown as a comment (WRONG) followed by
# the corrected, runnable version (RIGHT).

# ---------------------------------------------------------------
# Mistake 1: Forgetting the colon
# ---------------------------------------------------------------
# WRONG:
# if score > 90
#     print("Excellent!")

score = 95
if score > 90:  # RIGHT: colon required after the condition
    print("Excellent!")


# ---------------------------------------------------------------
# Mistake 2: Wrong indentation
# ---------------------------------------------------------------
# WRONG (inconsistent/missing indentation causes IndentationError):
# if score > 90:
# print("Excellent!")

if score > 90:
    print("Excellent!")  # RIGHT: 4 spaces of indentation


# ---------------------------------------------------------------
# Mistake 3: Single "=" vs double "=="
# ---------------------------------------------------------------
city = "Delhi"        # single "=" ASSIGNS a value to the variable
if city == "Delhi":   # double "==" COMPARES values
    print("City matched!")


# ---------------------------------------------------------------
# Mistake 4: Not normalizing input with .lower()
# ---------------------------------------------------------------
# WRONG: "Mumbai" and "mumbai" are treated as different strings
# user_city = input("Enter city: ")
# if user_city == "mumbai":
#     print("Match found")

user_city = input("Enter city: ").lower()  # RIGHT
if user_city == "mumbai":
    print("Match found")
else:
    print("No match")


# ---------------------------------------------------------------
# Mistake 5: Forgetting int() when comparing numbers
# ---------------------------------------------------------------
# WRONG: comparing a string directly to a number doesn't work
# age = input("Enter your age: ")
# if age > 18:        # TypeError: '>' not supported between str and int
#     print("Adult")

age = int(input("Enter your age: "))  # RIGHT
if age > 18:
    print("Adult")
else:
    print("Minor")
