# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""



#problem 16

def solve(n):
    """Solve the 16th Euler problem
    
    Return the sum of the digits of 2**n"""
    Num = 2**n
    Sum=0
    for x in str(Num):
        Sum+=int(x)
    return Sum

assert solve(15)==26 

print(solve(1000))

