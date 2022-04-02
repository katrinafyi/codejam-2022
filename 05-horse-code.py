#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decode' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING code
#  2. STRING_ARRAY morse_code
#

def decode(code, morse_code):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    m = dict(zip(morse_code, letters))
    print(m)
    words = code.split('/')
    print(words)
    x = []
    for w in words:
        print(w)
        x.append(''.join(m[c] for c in w.split(' ')))
    print(x)
    asdf = {
        'tbh': 'thoroughbred horse',
        'smh': 'shaking my head',
        'gtfo': 'galloping through fields occasionally',
        'idc': "i don't canter",
        'btw': 'big trough of water'
    }
    for i, y in enumerate(x):
        x[i] = x[i] if y not in asdf else asdf[y]
    return ' '.join(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    code0 = input()

    morse_code0 = []

    for _ in range(26):
        morse_code0_item = input()
        morse_code0.append(morse_code0_item)

    decoded = decode(code0, morse_code0)

    fptr.write(decoded + '\n')

    fptr.close()
