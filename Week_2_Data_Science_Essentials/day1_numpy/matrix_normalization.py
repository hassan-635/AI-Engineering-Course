import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Original MAtrix :")
print(matrix)

# min max normalization

min_max_normalized = (matrix - np.min(matrix))/(np.max(matrix) - np.min(matrix))

print("Min max normalization : ")
print(min_max_normalized)

# z score normalization (average becomes 0 and standar deviation becomes 1)

z_score_normalized = (matrix - np.mean(matrix))/np.std(matrix)

print("Z-Score normalization : ")
print(z_score_normalized)

# vector normalization / l2 normalization:

vector_normalized = matrix / np.linalg.norm(matrix)
print("Vector normalization : ")
print(vector_normalized)