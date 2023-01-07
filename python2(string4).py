# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:15:38 2023

@author: user
"""

#In python, strings can be stored in Double Quotes/Single Quotes
nameDQ = "Manju DQ"
print(type(nameDQ))

nameSQ = 'Manju SQ'
print(type(nameSQ))

#Access string content
name = 'Manju DS'
print(name[0])

#slicing
print(name[0:5])

#Modify string content
name = name + 'xyz' #You can concatinate
print(name)

#Replace function
name = name.replace(name, name.upper())
print(name)

#instance: Check for instance comparision
isinstance(name, str) 
isinstance(name, int)