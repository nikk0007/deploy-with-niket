# AND
age = 22
has_voter_id = True

is_eligible_to_vote = (age >= 18) and has_voter_id
print(is_eligible_to_vote)    # True

age = 16
is_eligible_to_vote = (age >= 18) and has_voter_id
print(is_eligible_to_vote)    # False — even if one false then the whole expression is false

# OR: 
has_upi = False
has_cash = True
has_card = False

can_pay = has_upi or has_cash or has_card
print(can_pay)    # True — as cash is available, you can pay

# False only when all the conditions are false:
has_upi = False
has_cash = False
has_card = False
can_pay = has_upi or has_cash or has_card
print(can_pay)    # False

# NOT: it reverses the boolean value of the expression
is_server_down = False
print(not is_server_down)    # True — server is up

is_verified = True
print(not is_verified)       # False
