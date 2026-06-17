def reverse_num(num):
    mystring = str(num)
    size = len(mystring)
    newString = ""

    while size > 0:
        newString += mystring[size-1]
        size = size - 1

    print(f"Reversed number: {newString}")

reverse_num(1234)