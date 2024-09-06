#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:05:03 2024

@author: bioinfo
"""

# Polynomial Regression
# If your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression.

# Polynomial regression, like linear regression, uses the relationship between the variables x and y to find the best way to draw a line through the data points.

import matplotlib.pyplot as plt
x = [20, 30 , 40, 50, 60]
y = [70,60,50,30,40]
plt.scatter(x,y)
plt.show()

# Example
# Import numpy and matplotlib then draw the line of Polynomial Regression:

import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
# R-Squared
# It is important to know how well the relationship between the values of the x- and y-axis is, if there are no relationship the polynomial regression can not be used to predict anything.

# The relationship is measured with a value called the r-squared.

# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

# Python and the Sklearn module will compute this value for you, all you have to do is feed it with the x and y arrays:
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

# Predict Future Values
# Now we can use the information we have gathered to predict future values.

# Example: Let us try to predict the speed of a car that passes the tollbooth at around the time 17:00:

# To do so, we need the same mymodel array from the example above:
    
#     Example
# Predict the speed of a car passing at 17:00:

import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

speed = mymodel(17)
print(speed)

