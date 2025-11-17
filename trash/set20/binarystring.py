def binary(n, s=""):
    if n == 0:
        print(s)
        return
    binary(n-1, s + "0")
    binary(n-1, s + "1")

n = int(input("Enter number of bits: "))
binary(n)
