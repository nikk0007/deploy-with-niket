import sys

# =============================================================================
# PART 1: SYNTAX vs SEMANTICS
# =============================================================================

# --- WHAT IS SYNTAX? ---
# Syntax = the grammar rules of Python.

score = 95
if score > 90:
    print("Distinction")


# --- WHAT IS SEMANTICS? ---
# Semantics = the meaning of what your code actually does at runtime.

# Example of a SEMANTIC ERROR:
original_price = 500
discount = 50

# The line below has no syntax error — Python will run it happily.
# But the logic is WRONG: we are ADDING the discount instead of subtracting it.
final_amount = original_price + discount   # Syntax: correct. Logic: wrong.
print("Wrong final amount:", final_amount) # Prints 550 — should be 450

# The correct version:
final_amount = original_price - discount   # Now the logic matches the intent
print("Correct final amount:", final_amount) # Prints 450
# sys.exit()
# Syntax errors are caught immediately (Python tells you on which line).
# Semantic bugs are invisible until you test your output — and harder to find.


# =============================================================================
# PART 2: COMMENTS
# =============================================================================

# --- SINGLE LINE COMMENT: use the # symbol ---
# Everything after # on that line is ignored by Python.

# This function calculates the GST on a given price
def calculate_gst(price):
    return price * 0.18    # GST rate in India is 18 percent

gst_amount = calculate_gst(1000)
print("GST on 1000:", gst_amount)  # 180.0


# --- MULTI-LINE COMMENT: use triple quotes """  """ ---
# Used to write longer explanations — typically placed just below a function
# or class definition to describe what it does.

"""
calculate_final_price
----------------------
Takes the base price of a product.
Adds GST at 18 percent.
Subtracts any applicable discount.
Returns the final amount the customer pays.
"""
def calculate_final_price(price, discount):
    gst = price * 0.18
    return price + gst - discount

print("Final price:", calculate_final_price(1000, 50))  # 1130.0

# --- WHAT TO WRITE IN COMMENTS ---
# This is a BAD comment — it adds zero value:
age = 19
if age >= 18:          # checking if age is greater than or equal to 18
    print("Eligible")

# This is a GOOD comment — it explains WHY, not WHAT:
if age >= 18:          # 18 is the legal voting age per Election Commission of India rules
    print("Eligible to vote")

# The comment should explain WHY — the reasoning, the rule, the context.
