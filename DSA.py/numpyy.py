import numpy as np

arr = np.random.randint(3, 55, (3, 3))

print(arr)

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))