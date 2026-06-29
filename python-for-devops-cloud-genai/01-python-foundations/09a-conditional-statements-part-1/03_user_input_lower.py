# Section 4: Taking User Input
# input() always returns a string, even if the user types a number.

city = input("Enter your city: ")
print("You typed:", city)
print("Type of input:", type(city))

# Problem: "Mumbai", "MUMBAI", "mumbai" are all different strings to Python.
# Solution: normalize with .lower()

city_normalized = input("Enter your city again: ").lower()

if city_normalized == "mumbai":
    print("Welcome to Mumbai!")
else:
    print("City not recognized.")
