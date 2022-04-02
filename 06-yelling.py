#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Yelling' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

import string

def Yelling(s):
    letters = ''.join(s.split())
    #letters = s
    num_letters = len(s)
    lower = set(string.ascii_lowercase)
    num_lower = sum(x in lower for x in s)
    
    p = 100 * num_lower / num_letters
    if p == 0: return "Acceptable."
    if 0 <= p < 15: return "WHAT WAS THAT?!"
    if 15 <= p < 25: return "SAY THAT AGAIN?!"
    if 25 <= p < 50: return "YELL IT LOUDER!"
    if 50 <= p < 65: return "I CAN'T HEAR YOU!!"
    if 65 <= p < 75: return "I THOUGHT I HEARD SOMETHING?!"
    return "WHY ARE YOU SO QUIET?"

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = Yelling(s)

    fptr.write(result + '\n')

    fptr.close()
