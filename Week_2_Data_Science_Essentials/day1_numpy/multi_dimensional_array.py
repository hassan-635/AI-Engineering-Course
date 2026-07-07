import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Original : ")
print(matrix)

# transpose:
transpose = matrix.T
print("Transpose : ")
print(transpose)

matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Second Matrix :")
print(matrix2)

print(f"Division\n{matrix/matrix2}")
print(f"Multiplication\n{matrix*matrix2}")
print(f"Addition\n{matrix+matrix2}")
print(f"Subtraction\n{matrix-matrix2}")