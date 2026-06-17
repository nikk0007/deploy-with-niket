# Write a function, my_add_func(), that takes a single integer as input and returns the sum of the integers from
# zero to the input parameter.

# The function should return 0 if a non-integer is passed in.

def my_add_func(n):
    result = 0
    try:
        result = sum(range(n + 1))

    except Exception as e:
        print("Error occurred: " + e)

    return result

print(my_add_func(5))        