#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'invert_matrix' function below.
#
# The function is expected to return a 2D_FLOAT_ARRAY.
# The function accepts 2D_INTEGER_ARRAY a as parameter.
#

def invert_matrix(x):
    a = x[0][0]
    b = x[0][1]
    c = x[1][0]
    d = x[1][1]
    det = a*d-b*c
    if det == 0: return [[0.0,0.0],[0.0,0.0]]
    
    r = lambda x: round(x, 2)
    return [
        [r(d/det), r(-b/det)], 
        [r(-c/det), r(a/det)]
    ]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    matrix = []

    for _ in range(2):
        matrix.append(list(map(int, input().rstrip().split())))

    result = invert_matrix(matrix)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
