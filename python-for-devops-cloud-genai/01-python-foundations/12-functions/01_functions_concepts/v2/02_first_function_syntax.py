# ============================================================
# 02_first_function_syntax.py
# Topic: First Function — Syntax, Define vs Call
# ============================================================

# Syntax:
#
#   def function_name(parameters):
#       # logic
#       return result
#
# def           → keyword that tells Python you are defining a function
# function_name → the name you give it (use snake_case)
# parameters    → inputs the function needs (optional)
# return        → the output the function sends back to the caller (optional)
#
# DEFINING  a function = writing the blueprint. Nothing runs yet.
# CALLING   a function = actually executing it.

# ---- Defining the function ----
# Nothing happens here. Python just registers this in memory.

def greet_new_engineer(name):
    print(f"Welcome, {name}. Your onboarding environment is ready.")
    print(f"Your SSH key and VPN credentials have been sent to your email.")
    print()

# ---- Calling the function ----
# Now it actually runs — once per call.

greet_new_engineer("Priya Sharma")
greet_new_engineer("Rahul Verma")
greet_new_engineer("Aisha Khan")

# One function. Three calls. Logic lives in one place.
# If the onboarding message changes — update the function once.
# All three automatically get the new message.


# ---- A slightly more useful onboarding function ----

def provision_new_engineer(name, team, access_level="read-only"):
    print(f"Provisioning engineer: {name}")
    print(f"  Team          : {team}")
    print(f"  Access Level  : {access_level}")
    print(f"  AWS IAM Role  : arn:aws:iam::123456789012:role/{team}-{access_level}")
    print(f"  Status        : Done")
    print()

provision_new_engineer("Priya Sharma",  "platform-engineering", "admin")
provision_new_engineer("Rahul Verma",   "data-engineering")
provision_new_engineer("Aisha Khan",    "security-ops", "read-write")
