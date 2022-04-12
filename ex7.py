#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:20:15 2022

@author: yousufmohammad
"""

filename = input("Input the Filename: ")
f_extns= filename.split(".")
print("The extension of the file is: " + repr(f_extns[-1]))
