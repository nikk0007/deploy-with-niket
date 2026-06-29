# Section 6 & 7: MATCH-CASE
# Mini Project: Mobile Recharge Plan Info System
#
# NOTE: match-case requires Python 3.10 or higher.
# If your version is older, either update Python or use if/elif instead.

plan = input("Enter plan type (daily/weekly/monthly/annual): ").lower()

match plan:
    case "daily":
        print("Daily Plan - Rs. 19 | 1GB data | Valid 1 day")
    case "weekly":
        print("Weekly Plan - Rs. 99 | 7GB data | Valid 7 days")
    case "monthly":
        print("Monthly Plan - Rs. 299 | 2GB/day | Valid 28 days")
    case "annual":
        print("Annual Plan - Rs. 2999 | 2GB/day | Valid 365 days")
    case _:
        print("Invalid plan type. Please choose from the options above.")

# ---------------------------------------------------------------
# Trace through it:
#   User types "Monthly" -> .lower() -> "monthly" -> 3rd case matches
#     -> prints monthly plan details
#   User types "quarterly" -> no case matches -> case _ runs
#     -> "Invalid plan type."
# ---------------------------------------------------------------

# Syntax reminder:
#
# match variable:
#     case "value_1":
#         ...
#     case "value_2":
#         ...
#     case _:
#         ...   # wildcard - runs if nothing else matched (like "else")
#
# Adding a new plan later (e.g. "yearly") just means adding one more
# case block - nothing else in the code needs to change.
#
# Compare this to the equivalent if/elif version:
#
# if plan == "daily":
#     ...
# elif plan == "weekly":
#     ...
# elif plan == "monthly":
#     ...
# elif plan == "annual":
#     ...
# else:
#     ...
#
# Both work. match-case just reads cleaner when there are many
# specific values to check against.
