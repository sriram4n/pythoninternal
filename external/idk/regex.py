import re
phone = input("Enter phone number: ")
email = input("Enter email: ")

if re.fullmatch(r'(\+?\d{1,3}[\s-]?)?\d{7,15}$',phone):
    print("Valid phone")
else:
    print("Invalid phone")

if re.fullmatch(r'[A-Za-z0-9._]+\@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$',email):
    print("Valid email")
else:
    print("Invalid email")
