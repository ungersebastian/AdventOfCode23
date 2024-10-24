# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:36:38 2024

@author: PC
"""

from typing import List
import math

with open('puzzle.txt','r') as file:
    lines = []
    for line in file:
        lines.append(str(line).split())
    result = []
    for t, d in zip(lines[0][1:], lines[1][1:]):
        t, d = int(t), int(d)
        t01 = math.ceil(t/2-(t**2 / 4 - (d+1))**0.5)
        t02 = math.floor(t/2+(t**2 / 4 - (d+1))**0.5)
        result.append(t02-t01+1)
        
        
        
r = 1
for v in result:
    r *= v

print(r)

#part2

import math

with open('puzzle.txt','r') as file:
    lines = []
    for line in file:
        lines.append("".join(str(line).split()[1:]))
    t, d = int(lines[0]), int(lines[1])
    t01 = math.ceil(t/2-(t**2 / 4 - (d+1))**0.5)
    t02 = math.floor(t/2+(t**2 / 4 - (d+1))**0.5)
    
    print(t02-t01+1)
        
        
        