#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'calculateScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_CHARACTER_ARRAY turns as parameter.
#

def calculateScore(turns):
    s = 0
    strikes = []
    spares = []
    
    
    ts = []
    for i, (f, s) in enumerate(turns):
        x = None
        if f == 'X':
            x = (10, None)
        if s == '/':
            s = 10 - int(f)
        if f == '-':
            f = 0
        if s == '-':
            s = 0
        
        if not x: 
            x = (int(f), int(s))
        ts.append(x)
    
    print(turns)
    turns = ts
    print(turns)
    
    
    class A(int):
        def __add__(self, x):
            print(self, '+', x)
            return A(super().__add__(x))
    s = A(0)
    for i, (fst, snd) in enumerate(turns):
        if fst == 10:
            strikes.append(i)
            snd = 0
        elif fst + snd == 10:
            spares.append(i)
        s += fst + snd
        
        
    print(strikes)
    print(spares)
    for i in strikes:
        try:
            if turns[i+1][0] == 10:
                s += 10
                s += turns[i+2][0]
            else:
                s += turns[i+1][0] + turns[i+1][1]
        except:
            pass
            
    for i in spares:
        if i+1 < len(turns):
            try:
                s += turns[i+1][0]
            except: pass
            
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    scores = []

    for _ in range(t):
        scores.append(list(map(lambda x: x[0], input().rstrip().replace('_', '0').split())))

    total = calculateScore(scores)

    fptr.write(str(total) + '\n')

    fptr.close()
