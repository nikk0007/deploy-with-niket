def sum_of_digits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)

    print(sum)

sum_of_digits(1234)