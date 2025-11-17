def AND(a,b):
    return a & b

def OR(a,b):
    return a | b

def NOT(a):
    return 1-a

def XOR(a,b):
    return a ^ b

print("And gate truth table")
print("A B | A AND B")
for i in [0,1]:
    for j in [0,1]:
        print(f"{i} {j} \t {AND(i,j)}")
