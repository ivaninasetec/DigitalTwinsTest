#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:43:13 2023

@author: pablo
"""

import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5]
value = [10, 12, 8, 14, 10, 11]
value2 = [12, 13, 9, 15, 11, 18]
plt.plot(time, value)
plt.plot(time, value2)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Evolution of values over time')
plt.show()




