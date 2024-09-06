#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:33:31 2024

@author: bioinfo
"""

# Data Distribution
# Earlier in this tutorial we have worked with very small amounts of data in our examples, just to understand the different concepts.

# In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.

# How Can we Get Big Data Sets?
# To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.

# Create an array containing 250 random floats between 0 and 5:

import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

# Histogram
# To visualize the data set we can draw a histogram with the data we collected.

# We will use the Python module Matplotlib to draw a histogram.

# Learn about the Matplotlib module in our Matplotlib Tutorial.

# Draw a histogram:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 50)

plt.hist(x, 5)
plt.show()

# Example
# Create an array with 100000 random numbers, and display them using a histogram with 100 bars:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100)

plt.hist(x, 100)
plt.show()
# Normal Data Distribution
# In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.

# In this chapter we will learn how to create an array where the values are concentrated around a given value.

# In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.

# ExampleGet your own Python Server
# A typical normal data distribution:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 10000)

plt.hist(x, 100)
plt.show()
