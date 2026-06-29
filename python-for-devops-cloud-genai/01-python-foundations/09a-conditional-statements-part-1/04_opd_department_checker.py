# Section 5: Mini Project 1 - OPD Department Checker
#
# Scenario: Today only two OPD departments are open at a government
# hospital - Ortho and Cardiology.
# If the patient asks for one of these, generate a token.
# Otherwise, tell them the OPD is closed today.

department = input("Enter department name: ").lower()

if department == "ortho" or department == "cardiology":
    print(f"Proceeding to {department} OPD. Token generated.")
else:
    print("Sorry, this OPD is closed today. Please visit tomorrow.")

# Concepts used here:
#   == (double equal)  -> comparison, NOT assignment
#   or operator         -> True if ANY one condition is True
#   f-string             -> f"...{variable}..." inserts variable value
#
# Try it:
#   Input "Cardiology" -> .lower() -> "cardiology" -> condition True
#   Input "Dentistry"  -> .lower() -> "dentistry"  -> condition False
