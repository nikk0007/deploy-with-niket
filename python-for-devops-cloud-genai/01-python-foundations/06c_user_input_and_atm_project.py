# =============================================================================
# FILE 3: Taking User Input & Mini Project — ATM Calculator
# =============================================================================

# This file covers:
# 1. How input() works
# 2. The critical type trap that catches every beginner
# 3. A complete mini project: ATM Calculator
# =============================================================================


# =============================================================================
# PART 1: THE input() FUNCTION
# =============================================================================
# input() pauses your program and waits for the user to type something.
# Whatever the user types, input() captures it and returns it as a value.
# You can pass a message string to input() — it will display that as a prompt.

import sys
# Basic usage:
# user_name = input("Enter your name: ")
# print("Hello,", user_name)


# --- THE MOST IMPORTANT RULE ABOUT input() ---
# input() ALWAYS returns a string — no matter what the user types.
# Even if the user types 500, Python receives it as the string "500", not the
# integer 500. This is the #1 mistake beginners make with input().

# Example:
marks = input("Enter your marks in mathematics ")
print(type(marks))    # <class 'str'>   ← always a string
print(int(marks) + 5)


# =============================================================================
# PART 2: THE STRING TRAP — WHY YOU MUST CONVERT INPUT
# =============================================================================
# Here is what happens when you forget to convert input to a number:

# WRONG approach — this produces the wrong result:
# a = input("Enter first amount: ")    # user types 500  → stored as "500"
# b = input("Enter second amount: ")   # user types 300  → stored as "300"
# print(a + b)
# Output: "500300"
#
# Python didn't add 500 + 300. It joined two strings: "500" + "300" = "500300".
# This is called string concatenation — the + operator on strings joins them
# rather than adding them numerically.
# Python didn't make a mistake. You gave it two strings — it treated them as strings.

# CORRECT approach — convert input to int before doing arithmetic:
# a = int(input("Enter first amount: "))    # "500" → 500
# b = int(input("Enter second amount: "))   # "300" → 300
# print(a + b)
# Output: 800 ✅

# The fix is simple: wrap input() inside int() or float() immediately.
# int()   → use when you expect a whole number (age, quantity, PIN, count)
# float() → use when you expect a decimal number (price, balance, temperature)


# =============================================================================
# PART 3: MINI PROJECT — ATM CALCULATOR
# =============================================================================
# Let's bring together everything from this lesson — variables, data types,
# type conversion, and user input — into one small working program.
#
# What this program does:
# - Takes the account holder's name
# - Takes the current account balance
# - Takes the withdrawal amount
# - Calculates a 2% service charge on the withdrawal
# - Prints a full transaction summary
#
# Run this file to use the ATM Calculator interactively.

print("=" * 40)
print("      Welcome to Python ATM")
print("=" * 40)

# Taking the account holder's name — no conversion needed, names are text
account_holder = input("Enter account holder name: ")

# Taking the balance — using float() because balances can have decimal values
balance = float(input("Enter your current balance (Rs.): "))

# Taking the withdrawal amount — also float for the same reason
withdrawal = float(input("Enter amount to withdraw (Rs.): "))

# Calculating the service charge
# 2% service charge is applied on every withdrawal
service_charge_rate = 0.02                       # constant — rate never changes
charge_amount = withdrawal * service_charge_rate # actual charge in rupees

# Total deducted = withdrawal amount + service charge
net_deduction = withdrawal + charge_amount

# Remaining balance after the transaction
remaining_balance = balance - net_deduction

# Printing the transaction summary
print("\n--- Transaction Summary ---")
print("Account Holder    :", account_holder)
print("Amount Withdrawn  : Rs.", withdrawal)
print("Service Charge 2% : Rs.", charge_amount)
print("Total Deducted    : Rs.", net_deduction)
print("Remaining Balance : Rs.", remaining_balance)
print("---------------------------")

# =============================================================================
# HOW THIS PROGRAM USES EVERYTHING YOU HAVE LEARNED:
# =============================================================================
#
# Variable creation:
#   account_holder, balance, withdrawal, service_charge_rate, charge_amount,
#   net_deduction, remaining_balance — each is a named container holding data.
#
# Data types in action:
#   account_holder → str  (text from input, no conversion needed)
#   balance        → float (decimal number, converted with float())
#   withdrawal     → float (decimal number, converted with float())
#   service_charge_rate → float (a literal decimal value)
#   charge_amount  → float (result of float * float)
#
# Type conversion:
#   float(input(...)) converts the string that input() returns into a float,
#   so arithmetic operations work correctly.
#
# Without type conversion, balance - net_deduction would crash with a TypeError
# because you cannot subtract a string from a string using the - operator.
#
# Naming conventions:
#   All variables use snake_case (lowercase, underscores between words).
#   The constant service_charge_rate is named descriptively.
#
# This is a complete, working program — built using only the concepts
# covered in this lesson. No loops, no functions, no imports needed.
