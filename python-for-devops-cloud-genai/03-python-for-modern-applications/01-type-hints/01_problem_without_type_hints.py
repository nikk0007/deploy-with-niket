# Question: What does this function expect?
# Can you tell just by reading the signature?

def process_booking(passenger, train, seat):
    """
    Nobody knows:
    - Is 'passenger' a name (str) or a passenger ID (int)?
    - Is 'seat' a number like 12 or a code like 'A1'?
    - What does this function return?
    """
    pass


# Same problem — different domain
def deploy_service(service, replicas, region):
    pass


# And another one
def send_alert(user, message, priority):
    pass


# ============================================================
# This is the daily reality in large Python codebases.
# As teams grow, this ambiguity costs hours in confusion.
# ============================================================
