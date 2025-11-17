def binarygen(n,prefix=""):
    if(n == 0):
        print(prefix)
        return
    binarygen(n-1,prefix + "0")
    binarygen(n-1,prefix + "1")

print(binarygen(2))