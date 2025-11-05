try:
    list = [2,3,4,5]
    print(list[9])
except IndexError:
    print("Index out of bound")

try:
    print(3 / 0)
except ZeroDivisionError:
    print("Cannot divide with 0")