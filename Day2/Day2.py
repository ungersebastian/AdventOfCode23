# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:54:19 2024

@author: PC
"""

from typing import List, Dict

color_list = ['red', 'green', 'blue']

def color_counter(color_list: List[str]) -> Dict[str, int]:
    result = {'red': 0, 'green': 0, 'blue': 0}
    for color in color_list:
        if 'red' in color:
            result['red'] = int(color.replace('red', ''))
        elif 'green' in color:
            result['green'] = int(color.replace('green', ''))
        elif 'blue' in color:
            result['blue'] = int(color.replace('blue', ''))
    return result

## Puzzle 1

color_limit = {'red': 12, 'green': 13, 'blue': 14}

result_sum = 0

with open('puzzle.txt', 'r') as file:
    for line in file:
        line_split = line.split(':')
        game_id = int(line_split[0][5:])
        draws = line_split[1].split(';')
        possible = True
        for d in draws:
            if possible:
                colors = color_counter( d.split(',') )
                for c in color_list:
                    if colors[c] > color_limit[c]:
                        possible = False
                        break
        if possible:
            result_sum += game_id
            
print(result_sum)
        
# Puzzle 2

minimum_power_list = []

with open('puzzle.txt', 'r') as file:
    for line in file:
        line_split = line.split(':')
        game_id = int(line_split[0][5:])
        draws = line_split[1].split(';')
        draw_list = {'red': [], 'green': [], 'blue': []}
        for d in draws:
            colors = color_counter( d.split(',') )
            for c in color_list:
                draw_list[c].append(colors[c])
        power = 1
        for c in color_list:
            power *= max(draw_list[c])
            
        minimum_power_list.append(power)
        
print(sum(minimum_power_list))
        
       