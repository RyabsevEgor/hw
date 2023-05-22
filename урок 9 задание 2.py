#ввод первого списка
print('Введите значения первого списка. В конце списка нажмите Enter')
a = set()
for i in range(100000):
  c = input()
  if c == '':
    break
  else:
    a.add(c)

#ввод вторго списка
print('Введите значения второго списка. В конце списка нажмите Enter')
b = set()
for i in range(100000):
  c = input()
  if c == '':
    break
  else:
    b.add(c)
print(len(a.union(b)))