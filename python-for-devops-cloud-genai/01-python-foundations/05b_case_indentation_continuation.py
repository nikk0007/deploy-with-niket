# =============================================================================
# FILE 2: Case Sensitivity, Indentation, Line Continuation & Multiple Statements
# =============================================================================

# =============================================================================
# PART 1: CASE SENSITIVITY
# =============================================================================

import sys


pincode = 110001    # variable named 'pincode' (all lowercase)
Pincode = 400001    # completely DIFFERENT variable named 'Pincode'
PINCODE = 560001    # yet another DIFFERENT variable named 'PINCODE'

print(pincode)      # 110001
print(Pincode)      # 400001
print(PINCODE)      # 560001


# All three print different values — because they ARE different variables.

# The most common mistake: defining a variable with one casing and calling it
# with a different casing.

total_marks = 450
# print(Total_marks)  # This line would crash: NameError: name 'Total_marks' is not defined

# --- THE FIX: FOLLOW A CONSISTENT NAMING CONVENTION ---
#
# Python developers follow these agreed-upon conventions everywhere:
#
# Variables and functions → snake_case
#   All lowercase letters. Words separated by underscores.
#   Example: total_marks, student_name, calculate_gst
#
# Constants (values that never change) → ALL_CAPS
#   All uppercase letters. Words separated by underscores.
#   Example: GST_RATE, MAX_ATTEMPTS, PI
#
# Classes → PascalCase
#   Every word starts with a capital letter. No underscores.
#   Example: StudentRecord, BankAccount, HttpRequest
#
# Pick one convention per category. Use it everywhere. Never mix randomly.

student_name = "Anjali Verma"    # snake_case — correct for a variable
GST_RATE = 0.18                  # ALL_CAPS — correct for a constant
# class BankAccount:             # PascalCase — correct for a class


# =============================================================================
# PART 2: INDENTATION
# =============================================================================

marks = 72

if marks >= 90:
    grade = "A+"           # 4 spaces — this line belongs INSIDE the if block
    print("Outstanding!")  # 4 spaces — also inside the if block
elif marks >= 75:
    grade = "A"
    print("Excellent!")
else:
    grade = "B"
    print("Good effort!")

print(f"Final Grade: {grade}")   # 0 spaces — OUTSIDE all blocks. Always runs.


# --- WHAT HAPPENS WITHOUT INDENTATION ---

# if marks >= 75:
# print("Good score!")        # ERROR — this line must be indented

# --- NESTED INDENTATION ---
# When you have a block inside another block, each level adds 4 more spaces.

score = 85
attempts = 2

if score >= 80:              # outer if — 0 spaces (top level)
    if attempts == 1:        # inner if — 4 spaces (inside outer if)
        print("Excellent score on the very first attempt!")   # 8 spaces
    else:                    # inner else — 4 spaces
        print("Excellent score!")                             # 8 spaces
else:                        # outer else — 0 spaces
    print("Keep practicing.")                                 # 4 spaces


# =============================================================================
# PART 3: LINE CONTINUATION
# =============================================================================

# Python gives you two ways to cleanly break a long line into multiple lines.

# --- METHOD 1: BACKSLASH \ ---
# Place a backslash at the end of the line to tell Python
# "this statement continues on the next line."

# Without line continuation this would be one long, hard-to-read line:
physics_marks = 88
chemistry_marks = 76
maths_marks = 92
english_marks = 85
computer_marks = 95

total_score = physics_marks + chemistry_marks + maths_marks \
+ english_marks + computer_marks

print("Total score:", total_score)  # 436

# Backslash also works inside conditions:
student_attendance = 80
assignment_submitted = True
fees_paid = True

if student_attendance >= 75 \
        and assignment_submitted == True \
        and fees_paid == True:
    print("Student is eligible to sit for the examination")

# CAUTION with backslash:
# If there is even a single accidental space AFTER the backslash \  (like this),
# Python will throw a SyntaxError. The backslash must be the very last character.


# --- METHOD 2: PARENTHESES () — preferred in modern Python ---

total_score = (
    physics_marks
    + chemistry_marks
    + maths_marks
    + english_marks
    + computer_marks
)
print("Total score (parentheses method):", total_score)  # 436
# sys.exit()
# This also works cleanly for function calls with many arguments:
# send_report(
#     student_name="Anjali Verma",
#     roll_number=42,
#     total_marks=487,
#     grade="A"
# )

# =============================================================================
# PART 4: MULTIPLE STATEMENTS ON ONE LINE
# =============================================================================

# Python normally expects one statement per line.
# But you CAN place multiple statements on a single line using a semicolon ;

# Standard way — one statement per line (recommended):
city = "Bengaluru"
population = 12000000
is_metro = True

# Multiple statements on one line using semicolons (legal, but avoid in production):
city = "Bengaluru"; population = 12000000; is_metro = True

# Where the semicolon is occasionally acceptable — quick debugging tests:
x = 10; y = 20; print(x + y)   # Quick throwaway test — fine here

# THE RULE FOR PRODUCTION CODE:
# One statement per line. Always.
# Readability is always more important than saving a few lines.

