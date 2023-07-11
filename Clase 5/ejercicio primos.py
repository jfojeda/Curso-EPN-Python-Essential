# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 20:26:27 2023

@author: jfoje
"""

def esprimo (num):
    for j in range(2,num):
        if num%j==0:
            return False
    return True
    print(num)




for i in range(1,20):
    if esprimo(i+1):
        print(i+1, end=" ")