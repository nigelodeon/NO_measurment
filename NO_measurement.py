

# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:22:55 2024

@author: AlsleNi
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = '/media/nik/Volume1/home/DATA/BV2+OHSC_test_240705.csv'

data = pd.read_csv(path,sep=',')
x = np.array([0., 1.56, 3.125, 6.25, 12.5, 25., 50., 100.])
names = {1:'Cali_1', 2:'Cali_2', 3:'BV2_2%', 4:'BV2_2%', 5:'BV2_10%', 6:'BV2_10%',
         7:'NMDA', 8:'NMDA', 9:'Cali_9'}
y1 = data['1']
y2 = data['2']
y3 = data['9']
y = data[['1','2','9']]
fit = np.polyfit(x,y.mean(axis=1), 1)
m,b = fit
# plt.plot(x, y, 'x', label='data')
# plt.plot(x, y2, 'x', label='data2')
# plt.plot(x, y1, '+', label='data3')
# plt.plot(x, m*x+b , 'r', label='fit')
# plt.le!gend()

# Lambert Beersches Gesetz:
# E = log(I/I0) ~ c_NO = m * c + b 
# c_No = E/m - b

bV_02pr = data[['3', '4']][:6].mean(axis=1)
bV_10pr = data[['5', '6']][:6].mean(axis=1)
plt.plot(bV_02pr/m -b, 'o', label='BV2 2 %')
plt.plot(bV_10pr/m -b, 'x', label='BV2 10 %')
plt
nmda1 = data[['7', '8']][:6].mean(axis=1)
plt.plot(nmda1/m -b, '+', label='NMDA')


plt.legend()

plt.show()