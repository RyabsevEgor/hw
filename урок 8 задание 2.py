N = int(input())
a = []
b = []
for i in range(N):
  a.append(int(input()))
b.append(a[N-1])
b.extend(a[:N-1])
print(b)