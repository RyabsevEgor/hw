a = input().split()
c = set()
b = []
count = 0
for i in range(len(a)):
  c.add(a[i])
  if len(c) > count:
    count = len(c)
    b.append('YES')
  else:
    b.append('NO')
print(b)