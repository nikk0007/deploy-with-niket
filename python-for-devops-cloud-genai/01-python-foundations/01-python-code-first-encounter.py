# Python code first encounter
# These are simple code snippets to demonstrate the use of Python in a real-world scenario.

# python codes reads like English sentences, making it easy to understand and write.
if transaction_count > 5:
    block_account()
   
   
# functions are reusable blocks of code that perform a specific task. They help in organizing code and making it more readable. 
def confirm_order():
    # confirm order

def assign_delivery_partner():
    # assign partner

def send_tracking_link():
    # send real-time tracking

def complete_delivery():
    # delivery marked as done
   
   
# functions can be called in a sequence to perform a complete task, such as processing an order. 
def process_order():
    confirm_order()
    assign_delivery_partner()
    send_tracking_link()
    complete_delivery()
    
def check_over_completion(balls_bowled):
    if balls_bowled == 6:
        start_new_over()


def verify_player(player):
    if not player.is_registered:
        register_player(player)
        
        
# conditional statements allow us to execute certain blocks of code based on specific conditions. They are essential for decision-making in programming.      
if not internet.is_connected:
    show_error("No internet connection")

if not pin.is_correct:
    show_error("Wrong PIN")

if not account.has_sufficient_balance:
    show_error("Insufficient balance")
    
# indentation is crucial in Python as it defines the scope of loops, functions, and other code blocks. Proper indentation ensures that the code is organized and executes correctly.
def verify_player(player):
    if not player.is_registered:
        register_player(player)   # runs only if the condition is true
    log_verification()            # always runs regardless of the condition
    

# classes are blueprints for creating objects. They encapsulate data and functions that operate on that data. Classes help in organizing code and promoting reusability.
class CricketPlayer:
    def __init__(self, name, jersey_number):
        self.name = name
        self.jersey_number = jersey_number

    def bat(self):
        print(f"{self.name} is batting")

    def field(self, position):
        print(f"{self.name} is fielding at {position}")
        
# objects are instances of classes. They represent real-world entities and can have attributes and behaviors defined by their class.
# In the example below, we create an object of the CricketPlayer class and call its methods to demonstrate its behavior.
# player1 = CricketPlayer(name="Virat Kohli", jersey_number=18)
player1 = CricketPlayer("Virat Kohli", 18)

# Properties:
player1.name  # Accessing the name property of player1
player1.jersey_number  # Accessing the jersey_number property of player1

# methods:
player1.bat()  # Calling the bat method of player1
player1.field("mid-on")  # Calling the field method of player1 with a position argument




