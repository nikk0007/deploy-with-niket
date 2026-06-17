# =============================================================================
# FILE 1: Variables — What They Are, How to Create Them & Naming Rules
# =============================================================================

# =============================================================================
# PART 1: CREATING AND ASSIGNING VARIABLES
# =============================================================================

pnr_number = "4521679803"    # variable named pnr_number, holding a string value
print(pnr_number)            # 4521679803


# --- REAL EXAMPLE: Hospital Patient Record System ---
# A single program can store many different kinds of data in separate variables.
import sys
patient_name = "Rohan Sharma"    # text data
patient_age = 34                 # whole number
body_temperature = 98.6          # decimal number
is_admitted = True               # True or False value

print(patient_name)        # Rohan Sharma
print(patient_age)         # 34
print(body_temperature)    # 98.6
print(is_admitted)         # True


# Notice: we stored four completely different types of data —
# and Python figured out each type automatically.


# =============================================================================
# PART 2: VARIABLE NAMING — RULES YOU MUST FOLLOW
# =============================================================================
# Break these rules and Python will throw an error immediately.

# RULE 1: Must start with a letter (a-z or A-Z) or an underscore _
#         Cannot start with a number.

# match_score1 = 100    # ✅ correct — starts with a letter
# _otp_code = 784512    # ✅ correct — starts with underscore
# 1match_score = 100    # ❌ SyntaxError — starts with a number

match_score1 = 100
_otp_code = 784512
print(match_score1)    # 100
print(_otp_code)       # 784512


# RULE 2: Can only contain letters, digits, and underscores.
#         No hyphens, spaces, @, #, $, or any other special character.

# metro_balance = 500     # ✅ correct
# metro-balance = 500     # ❌ SyntaxError — hyphen is not allowed
# @metro_card = 500       # ❌ SyntaxError — @ is not allowed

metro_balance = 500
print(metro_balance)    # 500


# RULE 3: Cannot use Python's reserved keywords as variable names.
# Reserved keywords are words Python already uses for its own purposes.
# Examples: print, input, type, if, for, while, True, False, None, and, or, not

# for = "savings"     # ❌ BAD — 'type' is a built-in Python function
# if = 500          # ❌ BAD — 'input' is a built-in Python function

# Use descriptive names instead:
account_type = "savings"    # ✅ correct
deposit_amount = 500        # ✅ correct
# sys.exit()

# =============================================================================
# PART 3: VARIABLE NAMING — BEST PRACTICES
# =============================================================================
# Good names make code readable — bad names make code a nightmare to maintain.

# BEST PRACTICE 1: Use descriptive, meaningful names.
# The name should tell you what the variable holds — without needing a comment.

x = 34               # bad — what does x mean?
patient_age = 34     # good — immediately clear

y = 98.6             # bad
body_temperature = 98.6    # good


# BEST PRACTICE 2: Use snake_case for multi-word variable names.
# snake_case = all lowercase, words separated by underscores.

otpexpirytime = 300        # bad — hard to read
otp_expiry_time = 300      # good — easy to read

metrocardbalance = 1500    # bad
metro_card_balance = 1500  # good


# BEST PRACTICE 3: Avoid single-letter names except inside loops.

i = 0        # acceptable inside a for loop — short loops are conventional
score = 0    # better for a standalone variable

# BEST PRACTICE 4: Constants (values that never change) → use ALL_CAPS.
# This is a signal to anyone reading the code: "do not modify this value."

GST_RATE = 0.18           # constant — GST rate is fixed
MAX_LOGIN_ATTEMPTS = 3    # constant — policy limit


# =============================================================================
# PART 4: CASE SENSITIVITY
# =============================================================================

# Example — Zomato delivery partners:
delivery_partner = "Arjun"
Delivery_Partner = "Vikram"
DELIVERY_PARTNER = "Suresh"

print(delivery_partner)      # Arjun
print(Delivery_Partner)      # Vikram
print(DELIVERY_PARTNER)      # Suresh

# All three print different names — because they are genuinely different variables.

