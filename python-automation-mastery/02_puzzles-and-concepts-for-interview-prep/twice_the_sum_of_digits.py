# given an integer N, returns the smallest integer greater than N,
# the sum of whose digits is twice as big as the sum of digits of N.

def twice_sum_of_digits(num):
    required_sum = 2*(sum_of_digits(num))
    result = num
    while True:
        result += 1
        if sum_of_digits(result) == required_sum:
            return result

def sum_of_digits(num):
    sum = 0
    mystring = str(num)
    for digit in mystring:
        sum += int(digit)
    
    return sum


print(twice_sum_of_digits(23))