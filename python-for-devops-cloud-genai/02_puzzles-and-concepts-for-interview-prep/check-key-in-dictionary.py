def key_exists(dictionary, key):
    return key in dictionary

# Example usage:
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(key_exists(my_dict, 'age'))  # Output: True
print(key_exists(my_dict, 'gender'))  # Output: False

print(my_dict["name"])
