'''
Изучить сложности алгоритмов, которые мы прошли на 3 и 4 занятии.
Для каждого алгоритма необходимо выписать его сложность и небольшое, 
пояснение на тему того, как данная сложность вычисляется.

'''
# создание массива случайных чисел
import random
n = 5
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)


# пузырек
for i in range(n):
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1],  arr[j]

#коктейльная сортировка
left_index = 0
right_index = n-1
while left_index <= right_index:
    for i in range(left_index, right_index, +1):
        left = arr[i]
        right = arr[i + 1]
        if left < right:
            arr[i] = right
            arr[i + 1] = left
    right_index -= 1
    for i in range(right_index,left_index,  -1):
        right = arr[i]
        rleft = arr[i - 1]
        if left < right:
            arr[i] = left 
            arr[i - 1] = right
    left_index -= 1

#вставка
for i in range(n):
    val= arr[i]
    j = i -1
    if j < 0:
        continue
    while val < arr[j]:
        arr[j + 1] = arr [j]
        j -= 1
    arr[j + 1] = val

#выбор
for i in range(n - 1):
    min_max_index = i
    for j in range(i + 1, n, 1):
        if arr[j] > arr[min_max_index]:
            min_max_index = j
    temp = arr[i]
    arr[i] = arr[min_max_index]
    arr[min_max_index] = temp