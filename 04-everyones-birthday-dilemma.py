#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY birthdays
#

def solve(n, birthdays):
    from collections import defaultdict
    days = {k: 0 for k in range(365)}
    for d in birthdays:
        days[d] += 1
    return min(days, key=lambda x: days[x])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n0 = int(input().strip())

    birthdays0 = []

    for _ in range(n0):
        birthdays0_item = int(input().strip())
        birthdays0.append(birthdays0_item)

    day = solve(n0, birthdays0)

    fptr.write(str(day) + '\n')

    fptr.close()
