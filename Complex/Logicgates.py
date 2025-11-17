# `• Implement Digital Logic Gates (AND, OR, NOT, EX-OR).

def AND(a,b):
    return a & b

def OR(a,b):
    return a | b

def NOT(a):
    return 1 - a

def XOR(a,b):
    return a ^ b

print("A B | A & B")
for i in [0,1]:
    for j in [0,1]:
        print(f"{i} {j} | {AND(i,j)}")

print("A B | A | B")
for i in [0,1]:
    for j in [0,1]:
        print(f"{i} {j} | {OR(i,j)}")
        
print("A | not A")
for i in [0,1]:
    print(f"{i}| {NOT(i)}")

print("A B | A XOR B")
for i in [0,1]:
    for j in [0,1]:
        print(f"{i} {j} | {XOR(i,j)}")