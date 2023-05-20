# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:16:34 2023

@author: Егор
"""

num = int(input())
if num > 0:
  a = 'положительное '
elif num < 0:
  a = 'отрицательное '
else:
  a = 'нулевое '

b = ''
if num%2 == 0 and num != 0:
  b = 'четное '
elif num%2 != 0 and num != 0:
  b = 'нечетное '

print(a,b,'число', sep = '')