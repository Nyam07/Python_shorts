n = int(input("Enter how many numbers you want in this series: "))

# first = 0
# second = 1

# for i in range(n):
#     print(first)
#     temp = first
#     first = second
#     second = temp + second


def recursive_fibonacci(n):
    if n <= 1:
        return n 
    else:
        return (recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

print('Fibonacci series:')

for i in range(n):
    print(recursive_fibonacci(i))