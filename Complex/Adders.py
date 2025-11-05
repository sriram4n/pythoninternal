def HalfAdder(a,b):
    sum = a ^ b
    carry = a & b
    return sum,carry

def FullAdder(a,b,c):
    sum = (a ^ b) ^ c
    carry = (a & b) | (b & c) | (a & c)
    return sum,carry

def ParallelAdder(A,B):
    carry = 0
    result = []
    for i in range(len(A) - 1, -1, -1):
        sum, carry = FullAdder(A[i] , B[i], carry)
        result.insert(0,sum)

    result.insert(0,carry)
    return result

