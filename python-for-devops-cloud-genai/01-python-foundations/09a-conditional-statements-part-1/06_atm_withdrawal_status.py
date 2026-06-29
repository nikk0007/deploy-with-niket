# Section 7: Mini Project 2 - ATM Withdrawal Status
#
# Scenario: Program an ATM to show different messages depending
# on the withdrawal amount entered by the user.

amount = int(input("Enter withdrawal amount (in rupees): "))

if amount <= 500:
    print("Dispensing cash. Small amount - instant processing.")
elif amount <= 10000:
    print("Dispensing cash. Standard withdrawal processed.")
elif amount <= 50000:
    print("High value withdrawal. OTP verification required.")
else:
    print("Amount exceeds daily limit. Visit the branch.")

# Why int()?
#   input() always returns a string. But we are comparing 'amount'
#   to numbers (500, 10000, 50000). You cannot compare a string to
#   a number in this way, so we convert with int() (or float()
#   if decimals are expected).
#
# Flow examples:
#   amount = 300     -> first if True       -> "small amount" message
#   amount = 8000     -> first elif True     -> "standard withdrawal"
#   amount = 25000    -> second elif True    -> "OTP required"
#   amount = 100000   -> all False, else runs -> "visit the branch"


# ---------------------------------------------------------------
# CHALLENGE FOR VIEWERS (mentioned in the outro of the video):
# Add a new condition so that if amount is exactly 0, the program
# prints: "Invalid amount. Please enter more than 0."
#
# Hint: this new check should run BEFORE the existing checks,
# since amount = 0 would otherwise satisfy "amount <= 500".
#
# Uncomment and complete the version below to try it yourself:
# ---------------------------------------------------------------

# amount = int(input("Enter withdrawal amount (in rupees): "))
#
# if amount == 0:
#     print("Invalid amount. Please enter more than 0.")
# elif amount <= 500:
#     print("Dispensing cash. Small amount - instant processing.")
# elif amount <= 10000:
#     print("Dispensing cash. Standard withdrawal processed.")
# elif amount <= 50000:
#     print("High value withdrawal. OTP verification required.")
# else:
#     print("Amount exceeds daily limit. Visit the branch.")
