#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    tallestHeight = 0
    count = 0
    for height in ar:
        if height > tallestHeight:
            tallestHeight = height
            count = 1
        elif height == tallestHeight:
            count += 1
    return count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)