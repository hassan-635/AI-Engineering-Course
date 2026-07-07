
import numpy as np

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8], 
                   [8, 7, 6, 5], 
                   [4, 3, 2, 1]])

matrix2 = matrix.T
print(matrix)

for i in range(0, 4):
    r_sum = np.sum(matrix[i])
    c_sum = np.sum(matrix2[i])
    print(f"{i+1}th row : {r_sum}")
    print(f"{i+1}th column : {c_sum}")


print("___________________________________________________________")


for i in range(0, 4):
    c_sum = 0
    for j in range(0, 4):
        c_sum += matrix[j][i]
    print(f"{i+1}th column : {c_sum}")