def Capitalize(str):
    capitalized = ""
    for word in str.split():
        capitalized += word[0].upper() + word[1:].lower() + " "
    return capitalized

print(Capitalize("tHis iS a wEird sTRingGg"))