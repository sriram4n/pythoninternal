def halfadder(a,b):
    sum = a ^ b 
    carry = a & b 
    return sum,carry

def fulladder(a,b,c):
    sum = (a^b)^c
    carry = (a&b) | (b&c) | (a&c)
    return sum,carry

def paralleladder(A,B):
    carry = 0
    result = []
    for i in range(len(A)-1,-1,-1):
        sum,carry = fulladder(A[i] , B[i], carry)
        result.insert(0,sum)
    result.insert(0,carry)
    return result

print("Truth table for half adder")
print("A B\tSUM\tCARRY")
for i in [0,1]:
    for j in [0,1]:
        sum,carry = halfadder(i,j)
        print(f"{i} {j}\t{sum}\t{carry}")

print("Truth table for full adder")
print("A B C\tSUM\tCARRY")
for i in [0,1]:
    for j in [0,1]:
        for k in [0,1]:
            sum,carry = fulladder(i,j,k)
            print(f"{i} {j} {k}\t{sum}\t{carry}")

print("Parallel adder:")
A = [0,1,0,1]
B = [0,1,0,1]
result = paralleladder(A,B)
print(result)