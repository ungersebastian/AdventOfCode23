# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:29:38 2024

@author: PC
"""

## Puzzle1

from typing import List, Dict
import numpy as np

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
    line = line.replace('\n', '')
    result = [1 if char=='*' else 0 for char in line  ]
    return result    
             
with open('puzzle.txt', 'r') as file:
    mask = []
    numbers = []
    for i, line in enumerate( file ):
        numbers.append(get_number_list(line, i))
        mask.append(get_mask(line))
    mask = np.array(mask)
    
    numbers = [res for line in numbers for res in line]
     
    rows, cols = mask.shape
    
    power = []
    for iline, line in enumerate(mask):
        for icol, val in enumerate(line):
            if val == 1:
                prod = 1
                np = 0
                for n in numbers:
                    if (
                            (n[0]-1 <= icol) and 
                            (n[1]+0 >= icol) and  
                            (n[2]-1 <= iline) and
                            (n[2]+1 >= iline)
                            ):
                        prod *= n[3]
                        np += 1
                if np == 2:
                    power.append(prod)
    print(sum(power))
    
