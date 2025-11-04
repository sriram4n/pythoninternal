def hasDupes(list1):
    unique = set()
    for element in list1:
        if(element in unique):
            return True
        else:
            unique.add(element)
    return False

list1 = [1,2,3,4,2]
if(hasDupes(list1)):
    print("Has dupes")
else:
    print("no dupes")