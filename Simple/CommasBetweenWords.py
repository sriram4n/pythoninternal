str = input("Enter word: ")
result = ""
for ch in str:
    result += ch + ","

print(result[:-1])