def cleanse(string):
    cleansed = ""
    for word in string.split():
        newword = word[0].upper() + word[1:].lower()
        cleansed += newword + " "
    return cleansed

sentence = "imPostEr amoNguS fUNGus"
print(cleanse(sentence))
