#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:04:20 2022

@author: yousufmohammad
"""

my_list = "apple,banana,cherry,papya".split(",")
my_list = ['apple', 'banana', 'cherry','papaya']
print(sorted(my_list, key = lambda x: x.count('a')))