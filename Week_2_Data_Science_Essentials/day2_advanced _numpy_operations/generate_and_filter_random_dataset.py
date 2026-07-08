
import numpy as np

np.random.seed(42)
ds = np.random.randint(1, 51, size=(5, 5))

print("Dataset : ")
print(ds)

ds[ds > 25] = 0
print("Filtered Dataset : ")
print(ds)

print(f"Sum : {np.sum(ds)}")
print(f"Mean : {np.mean(ds)}")
print(f"Deviation : {np.std(ds)}")