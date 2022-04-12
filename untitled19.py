#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:14:43 2022

@author: yousufmohammad
"""

import csv

inputfile = csv.reader(open('WHO-COVID-19-india-data_.csv','r'))

for row in inputfile:
    print (row)