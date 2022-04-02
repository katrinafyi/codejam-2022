#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'condensedFormula' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING atoms
#  2. INTEGER_ARRAY positions
#

def condensedFormula(atoms, positions):
    if len(positions) != len(set(positions)):
        return 'invalid'
    
    
    from collections import defaultdict
    counts = defaultdict(int)
    for a in atoms:
        counts[a] += 1
    
    c = counts['C']
    counts['C'] -= c
    counts['O'] -= len(positions)
    counts['H'] -= len(positions)
    
    hs = c * 2 + 2
    hs -= len(positions)
    
    counts['H'] -= hs
    
    print(counts, positions)
    
    if not all(1 <= p <= c for p in positions):
        return 'invalid'
    
    if max(counts.values()) > 0:
        return 'invalid'
    
    o = ''
    positions = set(positions)
    for i in range(c):
        i += 1
        if i == 1 or i == c:
            h = 3
        else:
            h = 2
        
        if i in positions:
            h -= 1
        
        o += 'CH'
        if h > 1:
            o += str(h)
        if i in positions:
            o += '(OH)'
            
    return o
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    atoms = input().strip()

    positions = list(map(int, input().rstrip().split()))

    result = condensedFormula(atoms, positions)

    fptr.write(result + '\n')

    fptr.close()
