n = int(input())
ans = n * n + 100
ans -= 200
ans *= ans
if (ans < 1000000):
	ans *= 2

'''
Ответ: O(1)
'''