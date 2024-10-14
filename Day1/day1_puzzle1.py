# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:24:30 2024

@author: basti
"""

### DAY 1

# puzzle 1

digits = []

with open(r'puzzle.txt', 'r') as file:
    for line in file:
        result = []
        for char in line:
            if char.isdigit():
                result.append(int(char))
        digits.append(10*result[0]+result[-1])
        
my_sum = sum(digits)

print('Puzzle 1:',my_sum)

# puzzle 2
from typing import List

digits = []

def find_all(line: str, pattern: str) -> List[int]:
    positions = []
    start = 0
    while True:
        pos = line.find( pattern, start )
        if pos > -1:
            positions.append(pos)
            start = pos+1
        else:
            break
    return positions

old = [ 'one','two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
new = [ '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open(r'puzzle.txt', 'r') as file:
    for line in file:
        result = {}
        for o, n in zip(old, new):
            findings = find_all(line, o) + find_all(line, n)
            for f in findings:
                result[f] = n
        first = int(result[min(result.keys())])
        last = int(result[max(result.keys())])
        digits.append(10*first + last)

my_sum = sum(digits)

print('Puzzle 2:',my_sum)
