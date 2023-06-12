
import random
n = 40
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

answer = -1
to_search = random.randint(1, 100)
print(to_search)
# интерполяционный поиск
#######################################################
arr.sort()
left = 0
right = len(arr)-1
while (left <= right and
        to_search >= arr[left] and
        to_search <= arr[right]):
    part1 = float(right - left) / (arr[right] - arr[left])
    part2 = to_search - arr[left]
    index = left + int(part1 * part2)
    if arr[index] == to_search:
        answer = index
        break
    if arr[index] < to_search:
        left = index + 1
    else:
        right = index - 1

######################################################
print(arr)
if answer >= 0:
    print('индекс числа', to_search,'-', answer)
else:
    print('числа', to_search, 'нет в списке' )


