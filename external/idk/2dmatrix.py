rows = int(input("Enter no. of rows: "))
cols = int(input("Enter no. of cols: "))
list = []
for i in range(rows):
    templist = []
    for j in range(cols):
        temp = int(input(f"Enter value of row {i} and col {j}: "))
        templist.append(temp)
    list.append(templist)

for row in list:
    for col in row:
        print(col,end="")
    print()