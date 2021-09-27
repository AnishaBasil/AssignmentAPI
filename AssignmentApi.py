#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 12:36:51 2021

@author: anishabasil
"""
import pandas as pd
import requests
## Get Request for 
jsonResponse = requests.get('https://itunes.apple.com/search?term=jack+johnson')

##Check for 200 status message 
jsonResponse.status_code
jsonResponse.json()
Dataframe = pd.DataFrame(jsonResponse.json())


## get request for Jack Johnson songs
jsonResponse2 = requests.get('https://itunes.apple.com/search?term=jack+johnson')
jsonResponse2 =jsonResponse2.json()

## Lists the results column
jsonResponseResults = jsonResponse2['results']