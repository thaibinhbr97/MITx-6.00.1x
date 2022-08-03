#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:52:06 2022

@author: thaibinhbr97
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []   

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


# # Same plot
# plt.plot(mySamples, myLinear)
# plt.plot(mySamples, myQuadratic)
# plt.plot(mySamples, myCubic)
# plt.plot(mySamples, myExponential)

# # Different plots
# plt.figure('lin')
# plt.xlabel('sample points')
# plt.ylabel('linear function')
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.plot(mySamples, myQuadratic)
# plt.figure('cub')
# plt.plot(mySamples, myCubic)
# plt.figure('exp')
# plt.plot(mySamples, myExponential)
# plt.figure('quad')
# plt.ylabel('quadratic function')

# plt.figure('lin')
# plt.clf()
# plt.ylim(0, 1000)
# plt.plot(mySamples, myLinear)
# plt.title('Linear')

# plt.figure('quad')
# plt.clf()
# plt.ylim(0, 1000)
# plt.plot(mySamples, myQuadratic)
# plt.title('Quadratic')

# plt.figure('cub')
# plt.title('Cubic')
# plt.figure('exp')
# plt.title('Exponential')

# plt.figure('lin quad')
# plt.clf()
# plt.subplot(211)
# plt.ylim(0,900)
# plt.plot(mySamples, myLinear, 'b--',label='linear', linewidth=2.0)
# plt.subplot(212)
# plt.ylim(0,900)
# plt.plot(mySamples, myQuadratic, 'ro',label='quadratic', linewidth=3.0)
# plt.legend()
# plt.title('Linear vs. Quadratic')

# plt.figure('cub exp')
# plt.clf()
# plt.subplot(121)
# plt.ylim(0,14000)
# plt.plot(mySamples, myCubic, 'r^',label = 'cubic')
# plt.subplot(122)
# plt.ylim(0,14000)
# plt.plot(mySamples, myExponential, 'r--',label = 'exponential')
# plt.legend(loc= 'upper left')
# plt.title('Cubic vs. Exponential')



plt.figure('cub exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'b',label = 'cubic')
plt.plot(mySamples, myExponential, 'r--',label = 'exponential')
plt.yscale('log')
plt.legend(loc= 'upper left')
plt.title('Cubic vs. Exponential')

plt.figure('cub exp linear')
plt.clf()
plt.plot(mySamples, myCubic, 'b',label = 'cubic')
plt.plot(mySamples, myExponential, 'r--',label = 'exponential')
plt.legend(loc= 'upper left')
plt.title('Cubic vs. Exponential')