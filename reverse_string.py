# MATHEMATICAL EXPRESSION

def reverse(string):
    reversed_string = ''
    for i in string:
        reversed_string = i + reversed_string
    print('Reversed string: ', reversed_string)


# RECURSION
def reverse_recursion(string):
    if len(string) == 1:
        return string
    else:
        return reverse_recursion(string[1:] + string[0])



string = input("enter a string: ")
# reverse(string)
str2 = reverse_recursion(string)

print(str2)