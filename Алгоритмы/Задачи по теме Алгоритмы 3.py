import random
import time

n = 10
arr = []
for i in range (n):
    arr.append(random.randint(1, 100))

print(arr)
a = max(arr)
b = min(arr)
arr[arr.index(a)],  arr[arr.index(b)] = b, a
print(arr)