# 1. Basic usage of range(): Generating numbers from 0 to 4
def basic_range():
    """Generate a sequence of numbers from 0 to 4 using range()"""
    print("Basic Range:")
    for i in range(5):
        print(i, end=" ")
    print("\n" + "-" * 30)


# 2. Using range(start, stop): Generating numbers from 2 to 9
def range_with_start_stop():
    """Generate a sequence of numbers starting from 2 to 9 using range(start, stop)"""
    print("Range with start and stop:")
    for i in range(2, 10):
        print(i, end=" ")
    print("\n" + "-" * 30)


# 3. Using range(start, stop, step): Generating numbers from 0 to 10 with a step of 2
def range_with_step():
    """Generate a sequence of numbers from 0 to 10 with a step of 2 using range(start, stop, step)"""
    print("Range with step (0 to 10, step 2):")
    for i in range(0, 11, 2):
        print(i, end=" ")
    print("\n" + "-" * 30)


# 4. Using range to generate a reverse sequence: Counting down from 10 to 1
def reverse_range():
    """Generate a reverse sequence using range(start, stop, step)"""
    print("Reverse Range (10 to 1):")
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("\n" + "-" * 30)


# 5. Using range to iterate over a list with indices
def iterate_list_with_range():
    """Use range() to iterate over the index of a list"""
    fruits = ["apple", "banana", "cherry", "date"]
    print("Iterating over list using range and len():")
    for i in range(len(fruits)):
        print(f"Index {i} has fruit: {fruits[i]}")
    print("-" * 30)


# 6. Using range to iterate over a list in reverse order
def iterate_list_reverse():
    """Iterate over a list in reverse order using range()"""
    fruits = ["apple", "banana", "cherry", "date"]
    print("Iterating over list in reverse using range():")
    for i in range(len(fruits) - 1, -1, -1):
        print(f"Index {i} has fruit: {fruits[i]}")
    print("-" * 30)


# 7. Using range to create a list of even numbers
def list_even_numbers():
    """Create a list of even numbers using range()"""
    even_numbers = list(range(0, 21, 2))  # Create a list of even numbers from 0 to 20
    print(f"List of even numbers: {even_numbers}")
    print("-" * 30)


# Main function to call all the above examples
if __name__ == "__main__":
    basic_range()                # 1. Basic range() example
    range_with_start_stop()      # 2. Using range(start, stop)
    range_with_step()            # 3. Using range(start, stop, step)
    reverse_range()              # 4. Using range to count down
    iterate_list_with_range()    # 5. Iterating over a list with range
    iterate_list_reverse()       # 6. Iterating over a list in reverse order
    list_even_numbers()          # 7. Creating a list of even numbers using range
