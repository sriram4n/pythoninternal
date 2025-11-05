# jupyternotebook
# Find the word with the most occurrences in a file
with open("Text1.txt","r") as f1:
    contents = f1.read()
    word_count = {}
    for word in contents.split():
        if(word not in word_count):
            word_count[word] = 1;
        elif(word in word_count):
            word_count[word] = word_count[word] + 1
    maxword = max(word_count, key = word_count.get)
    print(f"The max word is {maxword}, it occured {word_count[maxword]} times")