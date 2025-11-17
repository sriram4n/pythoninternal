def modify(sentence, word):
    result = ""

    for w in sentence.split():
        if (w != word):
            result += w + " "

    return result

sentence = input("Enter string: ")
word = input("Enter word to remove: ")
result = modify(sentence, word)
print(result)