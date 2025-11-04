def binary(n, s = ""):
    if n == 0:
        print(s)
        return
    binary(n-1, s = s + "0")
    binary(n-1, s = s + "1")

n = int(input("Enter size: "))
binary(n)