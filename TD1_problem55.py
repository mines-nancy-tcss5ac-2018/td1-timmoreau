# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:42:39 2018

@author: moreau122u
"""

def isPalindrome(Number):
    """Checks if a number is a Palindrome"""
    ListOfDigit=[int(d) for d in str(Number)]
    n=len(ListOfDigit)
    for i in range(n//2):
        if ListOfDigit[i]!=ListOfDigit[-(i+1)]:
            return(False)
    return(True)

def reverse(Number):
    """Returns the number with its digits reversed (e.g. 123 -> 321)"""
    L=list(reversed([a for a in str(Number)]))
    L=''.join(L)
    return (int(L))

def isLychrel(Number):
    """Checks if a number is a Lychrel number"""
    Number+=reverse(Number)
    n=0
    while n<50:
        if isPalindrome(Number):
            return False
        else:
            Number+=reverse(Number)
            n+=1
    return True

def solve(n):
    """Gives the answer of the 55th Euler problem"""
    c=0
    Ans=0
    while c<=n:
        if isLychrel(c):
            Ans+=1
        c+=1
    return Ans

assert reverse(453)==354
assert isPalindrome(4994)==True
assert isPalindrome(54)==False
assert isLychrel(4994)==True
assert isLychrel(47)==False
print(solve(10000))