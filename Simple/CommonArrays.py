import numpy as np 

arr1 = [2,3,4,5,6]
arr2 = [2,4,6,8]

common_value = np.intersect1d(arr1,arr2)
print("Common values in arr1 and arr2 are: ",common_value)