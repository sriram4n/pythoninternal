def checkpalindrome(str):
    return str == str[::-1]

str = input("Enter string: ")
if(checkpalindrome(str)):
    print("Paldinrome")
else:
    print("not palindrome")