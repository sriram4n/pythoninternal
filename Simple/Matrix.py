# Matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
rows = int(input("Enter no. of rows: "))
col = int(input("Enter no. of col: "))
Matrix = []
for i in range(rows):
    templist = []
    for j in range(col):
        templist.append(input(f"Enter value of {i},{j}: "))
    Matrix.append(templist)
print("Matrix is: ")
for rows in Matrix:
    for col in rows:
        print(col, end="")
    print()