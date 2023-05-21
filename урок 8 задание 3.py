m = int(input())
n = int(input())
A = []
for i in range(n):
  A.append(int(input()))
#сортировка по возрастанию
A.sort()
c = 0
while len(A)>1:
  sum = 0
  while sum + A[0] < m and len(A)>1:
    sum += A[0]
    del(A[0])
  c+=1

print('минимальное количество лодок:',c)