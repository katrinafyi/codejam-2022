#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a 2D_CHARACTER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER r
#  3. INTEGER c
#  4. 2D_CHARACTER_ARRAY grid
#

def adjs(pos):
    r,c = pos
    return [
        (r+1,c),
        (r-1,c),
        (r,c+1),
        (r,c-1),
        
        (r+1,c+1),
        (r-1,c+1),
        (r+1,c-1),
        (r-1,c-1)
    ]

def solve(n, r, c, grid):
    get = lambda p: grid[p[0]][p[1]]
    s = [(r,c)]
    seen = {(r,c)}
    #print(grid)
    while s:
        p = s.pop()
        
        for a in adjs(p):
            if get(a) != '1':
                continue
            if a in seen:
                continue
            s.append(a)
            seen.add(a)
    
    print(seen)
    
    walls = set()
    for s in seen:
        for a in adjs(s):
            r,c = a
            if grid[r][c] == '0':
                grid[r][c] = '#'
            
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n0 = int(input().strip())

    first_multiple_input = input().rstrip().split()

    r0 = int(first_multiple_input[0])

    c0 = int(first_multiple_input[1])

    grid0 = []

    for _ in range(n0):
        grid0.append(list(map(lambda x: x[0], input().rstrip().split())))

    res = solve(n0, r0, c0, grid0)

    fptr.write('\n'.join([' '.join(x) for x in res]))
    fptr.write('\n')

    fptr.close()
