#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toText' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

nums =     '_ one two three four five six seven eight nine'.split()
tens = 'ten eleven twelve thirteen fourteen fifteen sixteen ten-seven ten-eight ten-nine'.split()

ten_names = 'twenty thirty forty fifty'.split()

def toText(n):
    if n < 10:
        x = nums[n]
    elif 10 <= n <= 19:
        x = tens[n-10]
    elif 20 <= n <= 59:
        x = ten_names[n // 10 - 2]
        if n % 10 != 0:
            x += '-' + nums[n % 10]
    elif 60 <= n <= 79:
        x = 'sixty-' + toText(n - 60)
    elif n == 80:
        x = 'four-twenties'
    elif 81 <= n <= 99:
        x = 'four-twenty-' + toText(n-80)
    elif n == 100:
        x= 'one-hundred'
    
    if 20 <= n <= 80 and x.endswith('-one'):
        x = x.replace('-one', '-and-one')
        
    return x
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    word = toText(num)

    fptr.write(word + '\n')

    fptr.close()
