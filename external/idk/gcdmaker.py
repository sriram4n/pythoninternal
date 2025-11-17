def GCD(a,b):
    if(b==0):
        return a
    return GCD(b,a%b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = GCD(a,b)
print("GCD = ",result)
