item_price = 250
quantity = 4
total = item_price * quantity
discount = 75
amount_payable = total - discount

print("Total:", total)
print("After Discount:", amount_payable)

# Dicision / always returns a float even if the division is exact
print(10 / 5)     # 5.0
print(17 / 5)     # 3.4

# Floor division // returns the quotient in whole numbers, discarding the fractional part
print(17 // 5)    # 3

# Modulus operator % returns the remainder of the division
print(17 % 5)     # 2

# helpful for checking if a number is even or odd
number = 10
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Exponentiation **:
print(2 ** 10)    # 1024 — 2 multiplied by itself 10 times

