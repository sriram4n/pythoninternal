def check_sorted(list1):
    for i in range(len(list1) - 1):
        if(list1[i] > list1[i+1]):
            return False
    return True
my_list = [2,2,2,3,5]

if(check_sorted(my_list)):
    print("list is sorted")
else:
    print("list not sorted")
