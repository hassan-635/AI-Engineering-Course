import numpy as np

matrix = np.random.randint(0, 101, size = (10, 10))

print("Dataset : ")
print(matrix)

print("After Binary mask : ")
threshold = 50
mask = matrix > threshold # for true false
print(mask)
mask = np.where(matrix > 50, 1, 0) # for 0, 1
print(mask)