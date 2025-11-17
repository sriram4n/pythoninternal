n = int(input("Enter size of series: "))
first, current, next = 0, 0, 1

while n > 0:
    print(current, end=" ")
    first = current
    current = next
    next = first + next
    n -= 1
