#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:51:36 2022

@author: yousufmohammad
"""

def sum_thrice(x,y,z):
    sum = x + y + z
    if x == y == z:
        sum = sum*3
        return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
