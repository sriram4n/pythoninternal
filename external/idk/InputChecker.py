str = input("Enter input: ")

if str.isupper():
    print("Uppercase character")
elif str.islower():
    print("Lowercase character")
elif str.isdigit():
    print("Digit")
else:
    print("Special character")
