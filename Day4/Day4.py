# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:01:50 2024

@author: PC
"""

from typing import List

def str_to_numberlist(line: str) -> List[int]:
    return [int(x) for x  in line.split()]


result = []
with open('puzzle.txt', 'r') as file:
    for line in file:
        card = line.split(':')[1]
        set1, set2 = card.split('|')
        set1 = str_to_numberlist(set1)
        set2 = str_to_numberlist(set2)
        
        overlap = len(set(set1) & set(set2))
        if overlap > 0:
            result.append(2**(overlap-1))

print(sum(result))

# part 2

winning_dict = {}

with open('puzzle.txt', 'r') as file:
    for iLine, line in enumerate(file):
        iMax = iLine
        if iLine in winning_dict:
            winning_dict[iLine] += 1
        else:
            winning_dict[iLine] = 1
        n_copies = winning_dict[iLine]
        
        card = line.split(':')[1]
        set1, set2 = card.split('|')
        set1 = str_to_numberlist(set1)
        set2 = str_to_numberlist(set2)
        
        overlap = len(set(set1) & set(set2))
        if overlap > 0:
            for io in range(iLine+1, iLine + overlap + 1):
                if io in winning_dict:
                    winning_dict[io] += n_copies
                else:
                    winning_dict[io] = n_copies
    
    for i_rm in range(iMax+1, max(list(winning_dict.keys()))+1):
        print(i_rm)
        del  winning_dict[i_rm]
    
    print(sum(winning_dict.values()))