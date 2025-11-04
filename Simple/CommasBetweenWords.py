str = input("Enter word: ")
result = ""
for word in str:
    result += word + ","

print(result[:-1])