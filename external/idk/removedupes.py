def removedupes(ourlist):
    uniquelist = []
    for element in ourlist:
        if (element not in uniquelist):
            uniquelist.append(element)
    return uniquelist


mylist = [1,2,3,4,5,3,2,5,6,7,8,9,3,5,7,2,5,2]
withoutdupes = removedupes(mylist)
print("List without dupes : ",withoutdupes)