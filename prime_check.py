upper_level = int(input("Enter the upper level: "))
lower_level = int(input("Enter the lower level:"))

for i in range(lower_level, upper_level+1):
    check_prime(i)


def check_prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num%i) == 0:
                print(num, 'is not a prime number')
                break
        else:
            print(num, 'is a prime number')

    else:
        print(num, 'is not a prime number')
