import random
print('введите размерность через пробел')
a = list(map(int,input().split()))

def pl(t):
  for i in t:
    print(*i)

m1 = [[random.randint(-200,200) for i in range(a[0])] for i in range(a[1])]
m2 = [[random.randint(-200,200) for i in range(a[0])] for i in range(a[1])]

m3 = [[m1[i][j] + m2[i][j]  for j in range(a[0])] for i in range(a[1])] 

pl(m1)
print()
pl(m2)
print()
pl(m3)