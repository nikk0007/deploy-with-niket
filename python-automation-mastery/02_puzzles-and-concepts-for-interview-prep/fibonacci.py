def fibonacci(n):
    arr = [0, 1]
    for index in range(2, n+1):
        arr.append(arr[index-2] + arr[index-1])
    print(arr)

fibonacci(10)            