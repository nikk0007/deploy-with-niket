days_since_last_booking = 30
minimum_gap_required = 21

is_eligible = days_since_last_booking >= minimum_gap_required
print(is_eligible)    # True

entered_pin = "9182"
saved_pin = "9182"

print(entered_pin == saved_pin)    # True
print(entered_pin != saved_pin)    # False

city1 = "Delhi"
city2 = "delhi"
print(city1 == city2)    # False — its case-sensitive

current_temp = 42
safe_limit = 38

print(current_temp > safe_limit)    # True — heat alert!
print(current_temp < safe_limit)    # False

# Greater than or equal to aur Less than or equal to:
wallet_balance = 500
order_amount = 500

can_place_order = wallet_balance >= order_amount
print(can_place_order)    # True — you have just enough balance to place the order!

