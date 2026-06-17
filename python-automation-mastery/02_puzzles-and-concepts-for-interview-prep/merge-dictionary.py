def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# another method
def merge_dicts2(dict1, dict2):
    for key in dict2:
        if key not in dict1:
            dict1[key] = dict2[key]
    return dict1

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
