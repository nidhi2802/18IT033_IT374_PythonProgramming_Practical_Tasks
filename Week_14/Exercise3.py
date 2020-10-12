string1 = input("Enter a string: ")
string2 = string1[::-1]
if string1.lower()==string2.lower():
    print(string1,"is palindrome")
else:
    print(string1, "is not palindrome")

