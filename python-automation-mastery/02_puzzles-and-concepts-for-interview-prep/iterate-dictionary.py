def iterate_dictionary(dictionary):
    for key in dictionary:
        value = dictionary[key]
        print(f'{key}: {value}')

# Example usage:
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
iterate_dictionary(my_dict)
# Output:
# name: John
# age: 30
# city: New York
