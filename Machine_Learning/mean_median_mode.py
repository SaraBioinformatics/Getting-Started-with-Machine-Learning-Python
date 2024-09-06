#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:19:09 2024

@author: bioinfo
"""

# Mean, Median, and Mode
# What can we learn from looking at a group of numbers?

# In Machine Learning (and in mathematics) there are often three values that interests us:

# Mean - The average value
# Median - The mid point value
# Mode - The most common value
# Example: We have registered the speed of 13 cars:

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# What is the average, the middle, or the most common speed value?

# ExampleGet your own Python Server
# Use the NumPy mean() method to find the average speed:

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

# Median
# The median value is the value in the middle, after you have sorted all the values:

# 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
# Example
# Use the NumPy median() method to find the middle value:

import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

# Example Median
# Using the NumPy module:

import numpy

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

# Mode
# The Mode value is the value that appears the most number of times:

# 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

# The SciPy module has a method for this. Learn about the SciPy module in our SciPy Tutorial.

# Example
# Use the SciPy mode() method to find the number that appears the most:

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)
