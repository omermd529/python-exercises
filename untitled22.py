#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 19:47:50 2022

@author: yousufmohammad
"""

# Python program to illustrate
# creating a data frame using CSV files

# import pandas module
import pandas as pd
# import csv module
import csv

with open("WHO-COVID-19-india-data_.csv") as csv_file:
	# read the csv file
	csv_reader = csv.reader(csv_file)

	# now we can use this csv files into the pandas
	df = pd.DataFrame([csv_reader], index = None)

# iterating values of first column
for val in list(df[100]):
	print(val)
for x in csv_reader:
  print(x)
  if x == "IN":
    break