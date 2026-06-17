# Write a function to find and print all unique elements in a given list.

def find_unique_elements(lst):
    return set(lst)

print(find_unique_elements([1, 5, "hi", 5, "x", "hi"]))