num = int(input())
def factorial(i):
  a = 1
  for j in range(1,i+1):
    a *= j
  return a
n = factorial(num)
print(n)

def list_factorial(c):
  b = []
  for j in range(n,0,-1):
    b.append(factorial(j))
  return b
print(list_factorial(n))