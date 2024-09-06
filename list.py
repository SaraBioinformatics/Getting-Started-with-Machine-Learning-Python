#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:11:05 2024

@author: bioinfo
"""

# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:
a = ["apple", "banana", "mango"]
print(a)
print(len(a))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
thislist = ["apple", "banana", "cherry"]
print(thislist[2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:4])
      # Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[2] = "blackcurrant"
print(thislist)

# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Example
#Get your own Python Server
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Example
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
a = ["banana", "apple", "orange"]
a.insert(3, "cherry")
print(a)

# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86