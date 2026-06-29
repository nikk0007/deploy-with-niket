# Section 1 & 2: NESTED IF
# Mini Project: Exam Hall Entry System
#
# Student is allowed in ONLY if:
#   - exam is scheduled today, AND
#   - biometric is verified
#
# The inner check only happens if the outer check passes.

exam_scheduled = True
biometric_verified = False

if exam_scheduled:
    if biometric_verified:
        print("Entry granted. Proceed to your hall.")
    else:
        print("Biometric failed. Report to the help desk.")
else:
    print("No exam scheduled today. Centre is closed.")

# ---------------------------------------------------------------
# Trace through it:
#   exam_scheduled = True  -> outer if True  -> go inside
#   biometric_verified = False -> inner if False -> inner else runs
#   Output: "Biometric failed. Report to the help desk."
#
# Now try: exam_scheduled = False
#   Outer if is False -> outer else runs immediately
#   Output: "No exam scheduled today. Centre is closed."
#   The inner if never even executes - it's never reached.
# ---------------------------------------------------------------

# Syntax reminder:
#
# if outer_condition:
#     if inner_condition:
#         ...   # both True
#     else:
#         ...   # outer True, inner False
# else:
#     ...       # outer itself was False
#
# Indentation tells Python which "else" belongs to which "if".
