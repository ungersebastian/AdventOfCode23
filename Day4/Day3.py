# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:01:50 2024

@author: PC
"""

from typing import List

with open('puzzle.txt', 'r') as file:
    for line in file:
        card = line.split(':')[1]
        set1, set2 = card.split('|')
        