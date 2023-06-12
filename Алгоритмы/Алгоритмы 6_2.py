import random
n = 40
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

answer = -1
to_search = random.randint(1, 100)
print(to_search)

arr[1] = 0
# Решето Эратосфена
#######################################################
for i in range(n):
    if arr[i] != 0:
        j = i * 2
        while j < n: 
            arr[j] = 0
            j += i
######################################################

for elem in arr:
    if elem != 0:
        print(elem, end = ' ')