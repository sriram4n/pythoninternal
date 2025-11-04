# Write a python code to read dictionary values from the user.
# Construct a function to invert its content. i.e., keys should be values
# and values should be keys.
def invert_dict(d):
    inv = {}
    for key, value in d.items():
        inv[value] = key
    return inv


n = int(input("Enter number of items: "))
d = {}

for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    d[k] = v

print("Original dictionary:", d)
print("Inverted dictionary:", invert_dict(d))
