#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:57:50 2024

@author: bioinfo
"""

# Python If ... Else

# Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

# ExampleGet your own Python Server
# If statement:

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
#   Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# Example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#   Else
# The else keyword catches anything which isn't caught by the preceding conditions.

# Example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

# Example
# One line if statement:

if a > b: print("a is greater than b")