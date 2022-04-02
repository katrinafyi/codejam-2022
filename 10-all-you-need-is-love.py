#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'AllYouNeedIsLove' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def AllYouNeedIsLove(s):
    points = {'A': 0, 'B': 0}
    games = {'A': 0, 'B': 0}
    
    delta = lambda d: max(d.values()) - min(d.values())
    maxx = lambda d: max(d.values())
    winn = lambda d: max(d, key=d.__getitem__)
    
    # A positive, B negative.
    i = 0
    while i < len(s):
        c = s[i]
        points[c] += 1
        i += 1
        if maxx(points) >= 4 and delta(points) >= 2:
            w = winn(points)
            print(points)
            points = {'A': 0, 'B': 0}
            games[w] += 1
            print(games)
            print()
        
            if maxx(games) >= 6 and delta(games) >= 2:
                # win set
                return w
            elif maxx(games) == 6 and delta(games) == 0:
                break
        
        
    points = {'A': 0, 'B': 0}
    while i < len(s):
        c = s[i]
        points[c] += 1
        if maxx(points) >= 7:
            w = winn(points)
            return w
        i += 1
        
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = AllYouNeedIsLove(s)

    fptr.write(result + '\n')

    fptr.close()
