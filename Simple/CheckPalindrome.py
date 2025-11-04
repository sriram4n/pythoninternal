def checkpalindrome(str):
    rev = str[::-1]
    if(str == rev):
        return True
    else:
        return False

str = input("Enter string: ")
if(checkpalindrome(str)):
    print("Paldinrome")
else:
    print("not palindrome")