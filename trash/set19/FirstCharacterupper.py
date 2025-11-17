# # Write a function that takes a sentence as an input parameter and 
# replaces the first letter of every word with the corresponding upper case 
# letter and the rest of the letters in the word by corresponding letters in 
# lower case without using a built-in function?
def format_sentence(sentence):
    result = ""
    for word in sentence.split():
        new = word[0].upper() + word[1:].lower()
        result += new + " "
    
    return result


sentence = input("Enter sentence: ")
print(format_sentence(sentence))