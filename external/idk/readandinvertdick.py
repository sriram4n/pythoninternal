def invertdic(dic):
    invdic = {}
    for key,value in dic.items():
        invdic[value] = key
    return invdic


mydic = {}
n = int(input("Enter no. of pairs: "))
for i in range(n):
    key = input("Key: ")
    value = input("Value: ")
    mydic[key] = value

print("original dic:",mydic)
print("inverted dic:",invertdic(mydic))