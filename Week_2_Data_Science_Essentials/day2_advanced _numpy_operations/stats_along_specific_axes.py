import numpy as np

np.random.seed(20)
matrix = np.random.randint(0, 51, size=(3, 3))

print("Matrix : ")
print(matrix)

print(f"Sum along col : {np.sum(matrix, axis = 0)}")
print(f"Sum along row : {np.sum(matrix, axis = 1)}")

print(f"Mean along col : {np.mean(matrix, axis = 0)}")
print(f"Mean along row : {np.mean(matrix, axis = 1)}")

print(f"Std along col : {np.std(matrix, axis = 0)}")
print(f"Std along row : {np.std(matrix, axis = 1)}")
