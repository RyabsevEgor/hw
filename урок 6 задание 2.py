# -*- coding: utf-8 -*-
"""
Created on Sat May 20 21:19:44 2023

@author: Егор
"""
X = int(input())
c = 0
for i in range(1,X+1):
  if X%i == 0:
    c += 1
print(c)
