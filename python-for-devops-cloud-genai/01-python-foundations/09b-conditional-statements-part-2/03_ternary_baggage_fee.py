# Section 4 & 5: TERNARY OPERATOR
# Mini Project: Airport Baggage Fee Calculator
#
# Rule:
#   weight < 15 kg  -> no fee
#   weight >= 15 kg -> Rs. 500 fee

weight = int(input("Enter baggage weight in kg: "))

# ---------------------------------------------------------------
# Normal way (4 lines)
# ---------------------------------------------------------------
if weight < 15:
    baggage_fee = 0
else:
    baggage_fee = 500

print(f"[Normal if-else] Baggage fee: Rs. {baggage_fee}")

# ---------------------------------------------------------------
# Ternary way (1 line) - same logic, same result
# Syntax: value_if_true if condition else value_if_false
# ---------------------------------------------------------------
baggage_fee = 0 if weight < 15 else 500

print(f"[Ternary operator] Baggage fee: Rs. {baggage_fee}")

# Read it left to right:
# "Put 0 in baggage_fee if weight < 15 is True, otherwise put 500."

# ---------------------------------------------------------------
# Try it:
#   Input 12 -> Baggage fee: Rs. 0
#   Input 20 -> Baggage fee: Rs. 500
# ---------------------------------------------------------------

# Rule of thumb: use ternary only for SIMPLE one-condition assignments.
# If the logic gets more complex, go back to a normal if/elif/else -
# stuffing too much into a ternary makes code hard to read.

# Note: int() is needed because input() always returns a string,
# and we are comparing 'weight' against a number.
