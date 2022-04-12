#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:23:51 2022

@author: yousufmohammad
"""

import pandas as pd 
df = pd.read_csv("WHO-COVID-19-india-data_.csv")
substring = "2020"
df = df.reset_index()  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    if row["Date_reported"].find(substring) != -1:
        print(row )

        

print(type(df['Date_reported']))
ser = pd.Series(df['New_deaths']) 
data = ser.head(10)
data 
