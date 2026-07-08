import numpy as np

np.random.seed(42)
matrix = np.random.rand(5, 5)

print("Matrix : ")
print(matrix)

min_max_normalized = (matrix - np.min(matrix))/(np.max(matrix) - np.min(matrix))
z_score_normalized = (matrix - np.mean(matrix))/np.std(matrix)
vector_normalized = matrix/np.linalg.norm(matrix)

print("_____________________________________________________________")
print("Min max normalized : ")
print(min_max_normalized)
print("_____________________________________________________________")
print("Z Score normalized : ")
print(z_score_normalized)
print("_____________________________________________________________")
print("Vector normalized : ")
print(vector_normalized)