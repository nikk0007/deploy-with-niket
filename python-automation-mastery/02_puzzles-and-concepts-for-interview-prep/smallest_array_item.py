arr = [7, 5, 2, 9, 23]
smallest = arr[1]

for num in arr:
    if smallest > num:
        smallest = num

print(smallest)
print("using built in function: " + str(min(arr)))
