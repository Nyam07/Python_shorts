def get_gcd(a, b):
    if (a == 0):
        return b
    elif (b == 0):
        return a 

    # base case
    if(a == b):
        return a 
    
    if (a > b):
        return get_gcd(a-b, b)
    return get_gcd(a, b-a)


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if (get_gcd(a, b)):
    print("GCD of", a, "and", b, "is", get_gcd(a, b))
else:
    print('Not found')