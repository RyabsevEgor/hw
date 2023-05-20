# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:47:50 2023

@author: Егор
"""
word = input()
a = 0
e = 0
i = 0
o = 0

for j in range(len(word)):
  if word[j] == 'a':
    a += 1
  elif word[j] == 'e':
    e += 1
  elif word[j] == 'i':
    i += 1
  elif word[j] == 'o':
    o += 1


print('согласных букв', len(word)-(a+e+o+i))
print('гласных букв', a+e+o+i)

if a > 0:
  print('a =', a)
else:
  print('a =', 'False')

if e > 0:
  print('e =', e)
else:
  print('e =', 'False')

if i > 0:
  print('i =', i)
else:
  print('i =', 'False')

if o > 0:
  print('o =', o)
else:
  print('o =', 'False')
