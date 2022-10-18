str1= input("Enter the first string: ")
str2= input("Enter the second string: ")

def check(str1, str2):
    if sorted(str1) == sorted(str2):
        print(str1, "and", str2, "are anagrams")
    else:
        print(str1, "and", str2, "are not anagrams")

#check(str1, str2)

def check2(str1, str2):
    x = [str1[i] for i in range(0, len(str1))]
    x.sort()
    y = [str2[i] for i in range(0, len(str2))]
    y.sort()

    if x == y:
        print(str1, "and", str2, "are anagrams")
    else:
        print(str1, "and", str2, "are not anagrams")  


check2(str1, str2)