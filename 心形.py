# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 08:41:23 2019

@author: Lenovo
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import sin,pi,sqrt
from matplotlib import animation 
b=200
def f(a,b):
    m=0
    m=(abs(a))**(2/3)+0.9*sqrt(3.3-a**2)*sin(b*pi*a)
    return m
# =============================================================================
# x=np.arange(-sqrt(3.3),sqrt(3.3),0.001)
# y=[f(e,b) for e in x]
# plt.axis([-2,2,-1.7,2.5])
# plt.plot(x,y,'-',color='r')
# plt.show()
# =============================================================================
fig, ax = plt.subplots()
x=np.arange(-sqrt(3.3),sqrt(3.3),0.00001)
line,= ax.plot(x,f(x,200),color='r')
plt.axis([-2,2,-1.7,2.5])
a=1
def update(frame):
    line.set_ydata(f(x,3+frame*a))
    return line,
ani = animation.FuncAnimation(fig, update, 130,interval=50, blit=True)
plt.show()

