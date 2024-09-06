#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:54:51 2024

@author: bioinfo
"""

# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
print("Hello")
print('Hello')    
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])
#modify
# Python has a set of built-in methods that you can use on strings.

# Upper Case
# ExampleGet your own Python Server
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
b = "Hello World"
print(b.lower())
# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Example
# The strip() method removes any whitespace from the beginning or the end:trip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# String Concatenation
# # To concatenate, or combine, two strings you can use the + operator.

# ExampleGet your own Python Server
# Merge variable a with variable b into variable c

a = "Hello"
b = "World"
c = a + b
print(c)
# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:


age = 36
txt = f"My name is John, I am {age}"
print(txt)

