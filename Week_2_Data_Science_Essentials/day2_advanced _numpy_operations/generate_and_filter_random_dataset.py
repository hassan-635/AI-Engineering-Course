
import numpy as np

ds = np.random.randint(1, 51, size=(5, 5))

print("Dataset : ")
print(ds)

ds[ds > 25] = 0
print("Filtered Dataset : ")
print(ds)
