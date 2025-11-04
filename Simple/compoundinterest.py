import math
p = int(input("Enter principle: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

ci = p * pow(((1+r/100)),t)
pure_interest = ci - p

print("Interest: ",pure_interest)
print("Total: ",ci)