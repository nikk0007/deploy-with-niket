# Write a function to remove duplicates from a given list while preserving the original order of elements.

def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(remove_duplicates([1, 5, "hi", 5, "x", "hi", 5]))



