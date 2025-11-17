word = "apple banana"
commaed = ""
for char in word:
    commaed = commaed + char + ","
print(commaed[:-1])

print(",".join(word))