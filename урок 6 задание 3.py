# -*- coding: utf-8 -*-
"""
Created on Sat May 20 21:31:26 2023

@author: Егор
"""
A = int(input())
B = int(input())
c = ''
for i in range (A,B+1):
  if i%2 == 0:
    c+=str(i)+' '
print(c)
