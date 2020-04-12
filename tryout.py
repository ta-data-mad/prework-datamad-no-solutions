#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:28:41 2020

@author: Blanca
"""
"Init working directory as a git directory"




# import os

with open("example.txt", "w") as f:
    f.write("Hello world \n")
    f.write("How are you? \n")
    f.write("Im fine.")
    

with open("example.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

data = []

with open("/Users/Blanca/ironhack/weight_height.csv", "r") as f: 
    lines = f.readlines()
    for line in lines: 
        data.append(line.split()[0].split(","))
        
heights = []

for person in data[1:]:
    height = int(person[2])
    heights.append(height)
avg_height = sum(heights)/ len(heights)
print(avg_height)    