#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:25:17 2024

@author: bioinfo
"""

# What is Standard Deviation?
# Standard deviation is a number that describes how spread out the values are.

# A low standard deviation means that most of the numbers are close to the mean (average) value.

# A high standard deviation means that the values are spread out over a wider range.

# Example: This time we have registered the speed of 7 cars:

# speed = [86,87,88,86,87,85,86]

# ExampleGet your own Python Server
# Use the NumPy std() method to find the standard deviation:

import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)

# Example
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print(x)

# Example
# Use the NumPy var() method to find the variance:

import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)

# Example
# Get your own Python Server
# Use the NumPy percentile() method to find the percentiles:

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)
# What is the age that 90% of the people are younger than?

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print(x)