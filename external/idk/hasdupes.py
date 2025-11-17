def hasdupes(ourlist):
    controllist = []
    for element in ourlist:
        if(element in controllist):
            return True
        else:
            controllist.append(element)    
    return False

mylist = [1,2,4,6,8]
if(hasdupes(mylist)):
    print("has dupes")
else:
    print("no dupes")