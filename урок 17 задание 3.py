n = int(input())
m = int(input())
k = 1000
for i in range(n):
	for j in range(m):
		k += 100

for i in range(m):
	for j in range(m):
		k -= 100

'''
Ответ: O(n*m + m^2)
'''