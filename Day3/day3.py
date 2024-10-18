# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:29:38 2024

@author: PC
"""

## Puzzle1

from typing import List, Dict
import numpy as np

#def decrypt(line: str) -> List[List[int], List[int]]:
#    pass

def unique_symbols(line: str) -> List[str]:
    symbols = list(set(line))
    unique = []
    for v in symbols:
        if not v.isnumeric():
            unique.append(v)
    return unique

def get_numbers(line: str) -> List[int]:
    symbols = unique_symbols(line)
    for s in symbols:
        line = line.replace(s, '.')
    result = [int(char) for char in line.split('.') if char]
    return result

def get_number_list(line: str, y: int) -> List[int]:
    numbers = get_numbers(line)
    result = []
    n = -1
    start = 0
    end = 0
    in_number = False
    for i, c in enumerate(line):
        if c.isnumeric():
            if not in_number:
                n += 1
                start = i
                end = i + len(str(numbers[n]))
                result.append([start, end, y, numbers[n]])
                in_number = True
                
        else:
            in_number = False
    return result

def get_mask(line: str) -> List[int]:
    symbols = unique_symbols(line)
    symbols.remove('.')
    line = line.replace('\n', '')
    for s in symbols:
        line = line.replace(s, '+')
    result = [1 if char=='+' else 0 for char in line  ]
    return result    
                

with open('puzzle.txt', 'r') as file:
    mask = []
    numbers = []
    for i, line in enumerate( file ):
        mask.append(get_mask(line))
        numbers.append(get_number_list(line, i))
    mask = np.array(mask)
    numbers = [res for line in numbers for res in line]
    
    result = []
    rows, cols = mask.shape
    
    for  n in numbers:
        matrix = mask[max(0, n[2]-1) : min(cols-1, n[2]+2),
                      max(0, n[0]-1) : min(rows-1, n[1]+1)]
        if np.sum(matrix) > 0:
            result.append(n[3])
            
    print(sum(result))
    
