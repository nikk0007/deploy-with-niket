# ============================================================
# the below quirks are not bugs — they are just how computers handle numbers
# ============================================================

# The famous 0.1 + 0.2 quirk — happens in every programming language
import sys

print(0.1 + 0.2)             # 0.30000000000000004

# Fix it using round()
print(round(0.1 + 0.2, 2))   # 0.3

# ============================================================
# bool (Boolean)
# Only two values: True or False — capital first letter is mandatory
# ============================================================

# Example: Online Job Application Portal
is_form_submitted = True
is_eligible = False
has_experience = True

print(is_form_submitted)       # True
print(type(is_eligible))       # <class 'bool'>

# Boolean as the result of a comparison
cutoff_marks = 60
applicant_score = 75

qualified = applicant_score >= cutoff_marks
print(qualified)               # True
print(type(qualified))         # <class 'bool'>

# Internally, True = 1 and False = 0
print(True + True)             # 2
print(False + 1)               # 1

# bool() converts any value to True or False
print(bool(0))                 # False — zero is False
print(bool(1))  


print(bool(""))                # False — empty string is False
print(bool("Delhi"))           # True — any non-empty string is True
print(bool(None))              # False
