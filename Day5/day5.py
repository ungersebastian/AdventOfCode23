# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:16:38 2024

@author: PC
"""

from typing import List

def transfer(name_map: str, val: int) -> int:
    transfer_list = transfer_map[name_map]
    
    for  t in transfer_list:
        if val >= t[1] and val < t[1] + t[2]:
            return val - t[1] + t[0]

    return val

transfer_map = {}


with open('puzzle.txt', 'r') as file:
    for line in file:
        if line.startswith('seeds:'):
            seeds = [int(x) for x in line.split(':')[1].split()]
        else:
            if line == '\n':
                pass
            elif not line[0].isnumeric():
                name = line.split()[0]
                transfer_map[name] = []
            else:
                transfer_map[name].append([int(x) for x in line.split()])

map_names = list(transfer_map.keys())                
print()
for name in map_names:
    seeds = [transfer(name, s) for s in seeds]

print(min(seeds))