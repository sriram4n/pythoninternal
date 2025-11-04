n = int(input("Enter number: "))
for i in range(n,0,-1):
    for j in range((n+1) - i):
        print(i,end="")
    print()