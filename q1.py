#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:36:47 2022

@author: omer

"""

l = []
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
        print(i,end=',')
print("\b")
        