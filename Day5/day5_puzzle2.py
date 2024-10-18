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
    
    # alle maps aufsteigend sortieren (nach source)
    for name in map_names:
        transfer_map[name].sort(key = lambda x: x[1])
    
    # seeds aufsteigend sortieren
    seeds = [seeds[i:i+2] for i in range(0, len(seeds),2)]
    seeds.sort(key = lambda x: x[0])
    
    ####################
    for name in map_names:
    
        tm = transfer_map[name]
        stops = [[s[1], s[1]+s[2], -s[1]+s[0]] for s in tm]
        
        seeds.sort(key = lambda x: x[0])
        
        result = []
        
        for s in seeds:
            for stop in tm:
                if s[0] < stop[1]:
                    if s[0] + s[1] < stop[1]:
                        result.append(s)
                        s = [0,0]
                        break
                    else:
                        result.append([s[0], stop[1]-s[0]])
                        s = [stop[1], s[1] - (stop[1]-s[0])]
                if s[0] >= stop[1] and s[0] < stop[1] + stop[2]:
                    if s[0] + s[1] < stop[1] + stop[2]:
                        result.append([s[0]-stop[1]+stop[0], s[1]])
                        s = [0,0]
                        break
                    else:
                        result.append([s[0]-stop[1]+stop[0], stop[2] - (s[0] - stop[1])])
                        s = [stop[1]+stop[2], s[1] - (stop[2] - (s[0] - stop[1]))]
            if s[1] != 0:
                result.append(s)
        seeds = result        
    minloc = [s[0] for s in seeds]                
        
print(min(minloc))                
    
    