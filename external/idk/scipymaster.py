from scipy.linalg import solve
import numpy as np

x = np.array([[2,2],[3,4]])
y = np.array([7,6])

result = solve(x,y)
print("x = ",result[0])
print("y = ",result[1])