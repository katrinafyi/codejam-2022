#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insert' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING entry
#  2. STRING_ARRAY data
#

def insert(entry, data):
    
    data.sort()
    
    def go(i, l):
        print(i,l)
        if l == 1:
            return i
        
        m = i + l // 2
        
        if data[m] == entry:
            return m
        elif entry > data[m]:
            return go(m, i + l - m)
        else:
            return go(i, m - i)
    
    i = go(0, len(data))
    if i+1 < len(data) and data[i+1] >= entry:
        i += 1
    return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    record = input()

    n = int(input().strip())

    records = []

    for _ in range(n):
        records_item = input()
        records.append(records_item)

    index = insert(record, records)

    fptr.write(str(index) + '\n')

    fptr.close()
