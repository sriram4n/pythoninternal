import numpy as np
matrix1 = [
    [1,2,3],
    [3,4,5],
    [4,5,6]
]
array1 = np.array(matrix1)
inverted = np.invert(array1)
transpose = np.transpose(array1)
print("inverted : ",inverted)
print("Transpose : ",transpose)