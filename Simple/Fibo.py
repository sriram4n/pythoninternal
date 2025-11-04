first, current, next = 0,1,0
n = int(input("Enter number: "))
while(n != 0):
    print(first, end= " ")
    next = first + current
    first = current
    current = next
    n -= 1

