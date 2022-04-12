#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:50:45 2022

@author: yousufmohammad
"""

from urllib.request import urlopen
import pandas as pd
import requests

for i in range(0,10):
    url = f"https://data.smgov.net/resource/ia9m-wspt.json?$limit=10&$offset={i*10}"
    data = requests.get(url)
    if data:
        data = data.json()
        df = pd.json_normalize(data)
        df.to_csv(f'csvfile_{i}.csv', encoding='utf-8', index=False)  
    


