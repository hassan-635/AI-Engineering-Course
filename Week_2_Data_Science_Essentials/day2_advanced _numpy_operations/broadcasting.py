import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix)

vector = [1, 1, 1]

broadcasted_matrix = matrix + vector;

print("Boradcasted matrix : ")
print(broadcasted_matrix)

print("After multiplication by scalar : ")
multiplicated = broadcasted_matrix * 10;
print(multiplicated)

