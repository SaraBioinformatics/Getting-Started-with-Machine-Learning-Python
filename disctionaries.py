#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:54:15 2024

@author: bioinfo
"""

# ExampleGet your own Python Server
# Create and print a dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Example
# Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# ExampleGet your own Python Server
# Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
