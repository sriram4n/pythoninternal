import math
p = int(input("Enter principle: "))
r = float(input("Enter rate: "))
t = int(input("Enter time: "))

ci = p * pow(1+r/100,t)

print("Total: ",ci)
print("Compounded Interest: ",ci-p)