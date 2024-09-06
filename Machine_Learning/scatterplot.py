#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:36:14 2024

@author: bioinfo
"""

# Scatter Plot
# A scatter plot is a diagram where each value in the data set is represented by a dot.

# The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:
# ExampleGet your own Python Server
# Use the scatter() method to draw a scatter plot diagram:

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()

# Random Data Distributions
# In Machine Learning the data sets can contain thousands-, or even millions, of values.

# You might not have real world data when you are testing an algorithm, you might have to use randomly generated values.

# As we have learned in the previous chapter, the NumPy module can help us with that!

# Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.

# The first array will have the mean set to 5.0 with a standard deviation of 1.0.

# The second array will have the mean set to 10.0 with a standard deviation of 2.0:
import numpy 
import matplotlib.pyplot as plt
x = [10, 20,30,40,50]
y = [50,40,30,20,10]
plt.scatter(x,y)
plt.show()
# Example
# A scatter plot with 1000 dots:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()
