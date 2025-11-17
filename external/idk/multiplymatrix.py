import numpy as np
mat1 = [
    [1,2,3],
    [1,2,3],
    [1,2,3]
]
mat2 = [
    [3,2,1],
    [3,2,1],
    [3,2,1]
]
result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
# result = np.dot(mat1,mat2)

for i in range(len(mat1)):          # row of mat1
    for j in range(len(mat2[0])):   # column of mat2
        for k in range(len(mat2)):  # row of mat2
            result[i][j] += mat1[i][k] * mat2[k][j]

print(result)