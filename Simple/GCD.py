def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"GCD of {a} and {b} is {GCD(a, b)}")