# -*- coding: utf-8 -*-
"""
Created on Sat May 20 21:05:06 2023

@author: Егор
"""
N = int(input())
c = 0
for i in range(N):
  if int(input()) == 0:
    c+=1
print(c)
