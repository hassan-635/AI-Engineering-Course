import numpy as np

np.random.seed(20)
matrix = np.random.randint(0, 51, size=(3, 3))

print("Matrix : ")
print(matrix)

print(f"Sum along col : {np.sum(matrix, axis = 0)}")
print(f"Sum along row : {np.sum(matrix, axis = 1)}")
