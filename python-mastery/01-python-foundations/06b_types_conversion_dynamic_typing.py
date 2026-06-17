# =============================================================================
# FILE 2: Variable Types, Type Checking, Type Conversion & Dynamic Typing
# =============================================================================

# =============================================================================
# PART 1: THE 4 BASIC VARIABLE TYPES
# =============================================================================

# --- int (Integer) ---
# Whole numbers — no decimal point. Can be positive, negative, or zero.
# Used for counting, indexing, scores, ages, quantities.
import sys

total_wickets = 10
overs_bowled = 20
run_deficit = -45       # negative integers are valid
print(total_wickets)    # 10


# --- float (Floating point) ---
# Numbers with a decimal point.
# Used for measurements, averages, prices, temperatures.

match_average = 45.6
ticket_price = 299.50
gravity = 9.8
print(match_average)    # 45.6


# --- str (String) ---
# Text data. Must be enclosed in quotes — single ('...') or double ("...").
# Anything inside the quotes is treated as text, even if it looks like a number.

team_name = "India"
city = 'Mumbai'
otp = "784512"          # this looks like a number but it IS a string — it's in quotes
print(team_name)        # India
print(otp)              # 784512

# --- bool (Boolean) ---
# Only two possible values: True or False.
# Note: the T and F must be capitalized. true and false are NOT valid in Python.
# Used for flags, conditions, status checks.

is_captain = True
is_retired = False
print(is_captain)       # True


# =============================================================================
# PART 2: CHECKING THE TYPE — type() FUNCTION
# =============================================================================
# You can check what type Python assigned to any variable using type().
# This is very useful when debugging or when you are unsure about a variable's type.

print(type(total_wickets))    # <class 'int'>
print(type(match_average))    # <class 'float'>
print(type(team_name))        # <class 'str'>
print(type(is_captain))       # <class 'bool'>

# You can also call type() directly on a value (without storing it in a variable):
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>

# --- Practical use: checking an OTP ---
otp = "784512"
print(type(otp))        # <class 'str'>
# Even though 784512 looks like a number, the quotes make it a string.
# type() confirms this immediately.


# =============================================================================
# PART 3: TYPE CONVERSION
# =============================================================================
# Sometimes you have data in one type but need it in another.
# Python provides built-in functions to convert between types.
#
# int()   → converts to integer
# float() → converts to float
# str()   → converts to string
# bool()  → converts to boolean

# --- EXAMPLE: Metro Card Recharge System ---
# Imagine a user types their recharge amount. It arrives as a string.
# To do arithmetic with it, you must convert it to a number first.

recharge_amount = "500"                    # this is a string — came from user input
print(type(recharge_amount))              # <class 'str'>

actual_amount = int(recharge_amount)       # converted to integer
print(type(actual_amount))                # <class 'int'>
print(actual_amount + 100)                # 600 — arithmetic now works correctly


# --- str to float ---
fare = "45.75"
fare_as_float = float(fare)
print(fare_as_float + 10)    # 55.75


# --- int / float to str ---
# Useful when you want to join a number with text using concatenation.
balance = 1500
message = "Your balance is: " + str(balance)
print(message)    # Your balance is: 1500
sys.exit()

# --- WHEN CONVERSION FAILS: ValueError ---
# Not every conversion is possible. Python can convert "500" to an integer
# because "500" is numerically valid. But it cannot convert "Rahul" to an integer
# because "Rahul" has no numeric meaning.

card_holder = "Rahul"
# int(card_holder)    # ❌ ValueError: invalid literal for int() with base 10: 'Rahul'

# The line above is commented out so this file can run.
# If you uncomment it, Python will crash on that line with a ValueError.


# --- SAFE CONVERSION REFERENCE ---
# "500"   → int("500")   = 500   ✅ works — numerically valid string
# "45.6"  → float("45.6") = 45.6 ✅ works — numerically valid string
# "Delhi" → int("Delhi")          ❌ ValueError — text cannot become a number
# 42      → str(42)      = "42"  ✅ always works — any number can become a string
# 0       → bool(0)      = False ✅ zero is treated as False
# 1       → bool(1)      = True  ✅ any non-zero number is treated as True
# ""      → bool("")     = False ✅ empty string is treated as False
# =============================================================================