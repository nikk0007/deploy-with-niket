passenger_age = 25
has_valid_passport = True
has_confirmed_ticket = True
is_blacklisted = False

can_board = (
    (passenger_age >= 18) and
    has_valid_passport and
    has_confirmed_ticket and
    (not is_blacklisted)
)

print("Can board flight:", can_board)    # True

# passenger_age >= 18 → comparison operator → True
# has_valid_passport → already bool → True
# has_confirmed_ticket → already bool → True
# not is_blacklisted → not False → True
# all connected by AND → True and True and True and True → True

# if you make is_blacklisted = True 
# not is_blacklisted    # not True → False
# can_board = False