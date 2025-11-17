def issorted(list):
    for i in range(len(list) - 1):
        if(list[i] > list[i+1]):
            return False
    return True

list = [2,5,4,5]

if(issorted(list)):
    print("list is sorted")
else:
    print("list isnt sorted")