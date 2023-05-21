N = int(input())
s = input().split()
t = set()
for i in range(N):
  t.add(int(s[i]))
print(len(t))
