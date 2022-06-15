# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 00:13:58 2022

@author: carlos
"""

def fbn(n):
    a = 1
    b = 1
    c = 0
    
    if (n == 1):
       return 1
    if (n == 2):
      return 1

    for i in range(0,3) :
        c = a + b
        a = b
        b = c 
        return c

fibo=lambda a: fbn(a)
n=int(input("Intro valor R"))
print("estructurado", fibo(n))



fib = lambda n: n if n<=1 else fib(n-1)+fib(n-2)
n=int(input("Intro valor "))
print("recursivo : ",fib(n))