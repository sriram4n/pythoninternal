new = ""
word = input("Enter word: ")
for ch in word:
    new += ch + ","
print(new[:-1])  # Remove the last character (comma)