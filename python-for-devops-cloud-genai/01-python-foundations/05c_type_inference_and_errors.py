# =============================================================================
# FILE 3: Type Inference, Dynamic Typing & Common Syntax Errors
# =============================================================================

# =============================================================================
# PART 1: TYPE INFERENCE AND DYNAMIC TYPING
# =============================================================================
import sys

passenger_count = 180          # Python infers: this is an integer (int)
flight_number = "AI302"        # Python infers: this is a string (str)
ticket_fare = 4599.50          # Python infers: this is a decimal number (float)
is_delayed = False             # Python infers: this is a boolean (bool)

# --- CHECKING THE TYPE OF A VARIABLE: type() ---
print(type(passenger_count))   # <class 'int'>
print(type(flight_number))     # <class 'str'>
print(type(ticket_fare))       # <class 'float'>
print(type(is_delayed))        # <class 'bool'>


# --- DYNAMIC TYPING: THE TYPE CAN CHANGE AT RUNTIME ---

gate_number = 14               # Right now: gate_number is an integer
print(type(gate_number))       # <class 'int'>
print("Gate:", gate_number)    # Gate: 14

gate_number = "ABCD"            # Now reassigned to a string — completely legal in Python
print(type(gate_number))       # <class 'str'>
print("Gate:", gate_number)    # Gate: ABCD

# Dynamic typing is a powerful feature — but it can also create confusing bugs
# Example of what NOT to do:
score = 95          # score starts as an integer
score = "ninety-five"   # suddenly reassigned to a string — confusing!
# score + 5              # This would now crash: can't add int to str
#
# Best practice: keep a variable's type consistent throughout your code.
# Change it only when there is a deliberate and clear reason to do so.


# --- FOUR CORE TYPES YOU WILL USE CONSTANTLY ---

# int — whole numbers (no decimal point)
seats_available = 42
print(seats_available, "→", type(seats_available))     # 42 → <class 'int'>

# float — numbers with a decimal point
ticket_price = 299.50
print(ticket_price, "→", type(ticket_price))           # 299.5 → <class 'float'>

# str — text, always wrapped in quotes (single or double)
platform_name = "PRS"
print(platform_name, "→", type(platform_name))         # PRS → <class 'str'>

# bool — only two possible values: True or False (capital T and F)
is_ac_coach = True
print(is_ac_coach, "→", type(is_ac_coach))             # True → <class 'bool'>


# =============================================================================
# PART 2: COMMON SYNTAX ERRORS AND HOW TO FIX THEM
# =============================================================================

# --- ERROR 1: MISSING COLON AFTER if / for / while / def / class ---
# Python requires a colon at the end of every statement that opens a new block.
# Forgetting the colon is the #1 syntax error for beginners.

registration_open = True
# WRONG (commented out so this file can still run):
# if registration_open
#     print("Apply now")         # SyntaxError: expected ':'

# CORRECT:
if registration_open:            # colon is mandatory here
    print("Registration is open — apply now!")


# --- ERROR 2: INDENTATIONERROR ---
# Every block of code that follows a colon MUST be indented.
subjects = ["Maths", "Science", "English"]

# WRONG (commented out):
# for subject in subjects:
# print(subject)                 # IndentationError: expected an indented block

# CORRECT:
for subject in subjects:
    print(subject)               # 4 spaces — correctly inside the for loop


# --- ERROR 3: NAMEERROR — using a variable before it is defined ---
# WRONG (commented out):
# print(application_status)      # NameError: name 'application_status' is not defined
# application_status = "Approved"

# CORRECT — define first, use second:
application_status = "Approved"
print("Application status:", application_status)   # Application status: Approved


# --- ERROR 4: CASE MISMATCH (also a NameError) ---
my_score = 550

# WRONG (commented out):
# print(My_Score)             # NameError: name 'Total_Score' is not defined

# CORRECT — use the exact same casing you used when defining it:
print("My score:", my_score)   # My score: 550


# --- ERROR 5: MISSING CLOSING BRACKET ---
physics = 88
chemistry = 76
maths = 92
english = 85

# WRONG (commented out):
# result = (physics + chemistry + maths
#           + english          # SyntaxError: unexpected EOF while parsing

# CORRECT — always close every bracket you open:
result = (physics + chemistry + maths
          + english)             # closing bracket on this line
print("Result:", result)         # Result: 341