# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:12:24 2023

@author: Егор
"""
n = int(input())

n1 = n%10                   #единицы
n10 = n%100//10             #десятки
n100 = n%1000//100          #сотни
n1000 = n%10000//1000       #тысячи
n10000 = n%100000//10000    #десятки тысяч
print(n10**n1*n100/(n10000-n1000))