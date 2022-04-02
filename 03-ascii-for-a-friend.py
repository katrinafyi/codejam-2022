#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'ASCIIForAFriend' function below.
#
# The function is expected to return a FLOAT.
# The function accepts STRING s as parameter.
#

def ASCIIForAFriend(s):
    x = 0
    for c in s:
        x += ord(c)
    return round(x / len(s), 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = ASCIIForAFriend(s)

    fptr.write(str(result) + '\n')

    fptr.close()
