# Write a python code to read dictionary values from the user.
# Construct a function to invert its content. i.e., keys should be values
# and values should be keys.
def invertdic(dic):
    inv = {}
    for key , value in dic.items():
        inv[value] = key
    return inv

dic = {}
n = int(input("Enter size of dictionary: "))
for i in range(n):
    k = input("Key: ")
    v = input("Value: ")
    dic[k] = v

inverted = invertdic(dic)
print("Original dic: ",dic)
print("Inverted Dic: ",inverted)