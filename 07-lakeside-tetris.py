#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'UQBridges' function below.
#
# The function is expected to return an INTEGER.
#

def UQBridges():
    l, w = input().split()
    m, n = input().split()
    l = int(l)
    w = int(w)
    m = int(m)
    n = int(n)
    b = min(l-m, w-n)
    return b*n + b*m + b*b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = UQBridges()

    fptr.write(str(result) + '\n')

    fptr.close()
