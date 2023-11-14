#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:49:43 2023

@author: pablo
"""

import requests


base_url= 'http://127.0.0.1:5000'#https://database.pcalleja.linkeddata.es/
url = base_url+'/users'
response = requests.get(url)
print(response.json())






import requests
#url = 'https://database.pcalleja.linkeddata.es/users'
url = base_url+'/users'
data =  {
    "classes": [
      {
        "name": "Programming"
      }
    ],
    "name": "María",
    "status": "professor",
    "user": "mpoveda"
  }
response = requests.post(url,json=data)
print(response.json())