# Using append() method
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Appending list2 as a single element to list1
list1.append(list2)

print("Using append():")
print("list1:", list1)  # Output: list1: [1, 2, 3, [4, 5, 6]]
print("list2:", list2)  # Output: list2: [4, 5, 6]

# Using extend() method
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Extending list1 with the elements of list2
list1.extend(list2)

print("\nUsing extend():")
print("list1:", list1)  # Output: list1: [1, 2, 3, 4, 5, 6]
print("list2:", list2)  # Output: list2: [4, 5, 6]
