# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:34:56 2018

@author: moreau122u
"""


#problem 22


def solve(FileName):
    """Solve the 22nd Euler problem"""
    File=open(FileName+'.txt','r')
    NameList=sortedFile(File)
    Total=0
    NamePosition=1
    for Name in NameList:
        String=list(Name)
        NameScore=sum(ord(x)-64 for x in String)
        Total+=NamePosition*NameScore
        NamePosition+=1
    return Total

def sortedFile(File):
    """Creates a sorted list out of a file containing a list of names surrounded with " """
    Lines=[]
    for Line in File:
        Lines.append(Line)
    NameList=str.split(Lines[0], '","')
    NameList[0]=NameList[0].replace('"','')
    NameList[-1]=NameList[-1].replace('"','')
    return sorted(NameList)


print(solve('p022_names'))