#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:41:56 2022

@author: yousufmohammad
"""

from datetime import date
f_date = date(2014,7,2)
l_date = date(2022,3,3)
delta = l_date - f_date

print(delta.days)
