def RemoveDupes(list1):
    uniqlist = []
    for element in list1:
        if(element not in uniqlist):
            uniqlist.append(element)
    return uniqlist

list1 = [1,2,3,4,4,3,5,2,49,0,0,0]
uniq = RemoveDupes(list1)
print(uniq)