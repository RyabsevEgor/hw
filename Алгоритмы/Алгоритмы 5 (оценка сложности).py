'''
Изучить сложности алгоритмов, которые мы прошли на 3 и 4 занятии.
Для каждого алгоритма необходимо выписать его сложность и небольшое, 
пояснение на тему того, как данная сложность вычисляется.

'''
# создание массива случайных чисел
import random


#создание массива чисел
n = 5 
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)
                                                            


# пузырек
for i in range(n):                                          # n                 основной цикл
    for j in range(n - 1):                                  # (n-1)             цикл внутри основного
        if arr[j] > arr[j + 1]:                             # 
            arr[j], arr[j + 1] = arr[j + 1],  arr[j]        # 
                                                            # n*(n-1) = n^2 - n   O(n^2)

#коктейльная сортировка
left_index = 0
right_index = n-1
while left_index <= right_index:                            # n (максимум n раз) основной цикл
    for i in range(left_index, right_index, +1):            # n1                   цикл 1 внутри основного
        left = arr[i]                                       #
        right = arr[i + 1]                                  #
        if left < right:                                    #
            arr[i] = right                                  #
            arr[i + 1] = left                               #
    right_index -= 1                                        #
    for i in range(right_index,left_index,  -1):            # n2                   цикл 2 внутри основного
        right = arr[i]                                      #
        rleft = arr[i - 1]                                  # 
        if left < right:                                    #
            arr[i] = left                                   # 
            arr[i - 1] = right                              # n1+n2 = n            всего действий по первому и второму циклу
    left_index -= 1                                         # n*(n1 + n2) = n^2     O(n^2)

#вставка
for i in range(n):                                          # n                 основной цикл
    val = arr[i]                                            #
    j = i - 1                                               #
    if j < 0:                                               #
        continue                                            #
    while val < arr[j]:                                     # n (максимум n раз)   цикл внутри основного
        arr[j + 1] = arr [j]                                #
        j -= 1                                              #
    arr[j + 1] = val                                        # n*n                      O(n^2)

#выбор
for i in range(n - 1):                                      # n - 1 основной цикл
    min_max_index = i                                       #
    for j in range(i + 1, n, 1):                            # n - 1 цикл внутри основного
        if arr[j] > arr[min_max_index]:                     #
            min_max_index = j                               #
    temp = arr[i]                                           #
    arr[i] = arr[min_max_index]                             #
    arr[min_max_index] = temp                               # (n-1)*(n-1) = n^2 - 2n + 1   O(n^2)

#шелла
step = len(arr) // 2                                                       #
while step > 0:                                                            # log2(n)  (сколько раз длина списка поделится на 2)
    for i in range(step, n, 1):                                            # log2(n)
        value = arr[i]                                                     #
        current_index = i                                                  #
        index_to_check = current_index - step                              #
        while current_index > 0 and arr[index_to_check] > value:           # n
            current_index -= step                                          #
            index_to_check -= step                                         #
        arr[current_index] = value                                         # 
    step = step // 2                                                       # n*log2(n)*log2(n)   O n*(log2(n))^2
    

#слияние
def  merge(arrl,arrr):                                                      
    sorted_arr = list()                                                     
    current_left = 0
    current_right = 0
    lenL = len(arrl)
    lenR = len(arrr)
    for i in range(lenL + lenR):
        if current_left < lenL and current_right < lenR:
            if arrl[current_left]> arrr[current_right]:
                sorted_arr.append(arrl[current_left])
                current_left += 1
            else:
                sorted_arr.append(arrr[current_right])
                current_right += 1
        else:
            if current_left == lenL:
                for j in range(current_right, lenR):
                    sorted_arr.append(arrr[j])
            else:
                for j in range(current_left, lenL):
                    sorted_arr.append(arrl[j])
            break
    return sorted_arr

def merge_sort(arr):                                        
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_side = list()
    right_side = list()
    
    for i in range(0, mid):
        val = arr[i]
        left_side.append(val)

    for i in range(mid, len(arr)):
        val = arr[i]
        right_side.append(val)

    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    result = merge(left_side, right_side)
    return result                          # 3*(2^(n/3) - 1)  (3 раза вызывается функия внутри себя)           O(2^n)

merge_sort(arr)                             

# быстрая сортировка

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    index_of_strong_elem = random.randint(0, len(arr))
    strong_elem = arr[index_of_strong_elem]
    low = list()
    mid = list()
    high = list()

    for elem in arr:
        if elem == strong_elem:
            mid.append(elem)
        elif elem < strong_elem:
            low.append(elem)
        else:
            high.append(elem)
    low = quick_sort(low)
    high = quick_sort(high)
    result = low + mid + high

    return(result)                        # 2*(2^(n/2) - 1)  (2 раза вызывается функия внутри себя)           O(2^n)
