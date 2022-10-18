def factorial(n):
    result = 0
    if n == 1:
        return 1
    
    else:
        result = n * factorial(n-1)

        return result


print("Factorial of 3 is:", factorial(3))