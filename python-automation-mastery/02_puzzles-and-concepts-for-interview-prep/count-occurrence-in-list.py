def count_names(names_list):
    name_count = {}
    for name in names_list:
        name_count[name] = name_count.get(name, 0) + 1
    return name_count

# Example usage:
names_list = ['John', 'Alice', 'Bob', 'John', 'Alice', 'Alice', 'John', 'Charlie']
result = count_names(names_list)
print(result)
# Output: {'John': 3, 'Alice': 3, 'Bob': 1, 'Charlie': 1}
