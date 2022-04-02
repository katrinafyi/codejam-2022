#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesar' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING pt
#

import string
def caesar(n, pt):
    o = ''
    for c in pt:
        if c not in string.ascii_letters:
            o += c
        elif c in string.ascii_uppercase:
            o += chr(ord('A') + (ord(c) - ord('A') + n) % 26)
        else:
            o += chr(ord('a') + (ord(c) - ord('a') + n) % 26)
    # Write your code here
    return o

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rotation = int(input().strip())

    plaintext = input()

    ciphertext = caesar(rotation, plaintext)

    fptr.write(ciphertext + '\n')

    fptr.close()
