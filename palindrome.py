string = input("Enter a string: ")

rev_string = string[::-1]

if string == rev_string:
    print("This is a palindrome")
else:
    print('This is not a palindrome')


number = int(input("Enter a Number: "))
string = str(number)

rev_string = string[::-1]

if string == rev_string:
    print("This is a palindrome")
else:
    print('This is not a palindrome')
