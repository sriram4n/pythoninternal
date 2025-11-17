mylist = [1,2,34,5,2,5,6,8,6,7,1]

for i in range(len(mylist) - 1):
    for j in range(len(mylist) - 1 - i):
        if(mylist[j] > mylist[j+1]):
            temp = mylist[j]
            mylist[j] = mylist[j+1]
            mylist[j+1] = temp

print(mylist)