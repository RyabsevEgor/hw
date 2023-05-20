# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:56:34 2023

@author: Егор
"""
X = int(input())
A = int(input())
B = int(input())
if A>=X and B>=X:
  print(2)
elif A>=X and B<=X:
  print('Mike')
elif A<=X and B>=X:
  print('Ivan')
elif A<=X and B<=X and A+B>=X:
  print(1)
else:
  print(0)
