def isPrime(n):
    if n < 2:
        return("Not Prime")
    else:
        for x in range(2, n):
            if n%x == 0:
                return("Not Prime")
            
        return("Is Prime")


print(isPrime(6))