#!/bin/python

import sys

def aVeryBigSum(n, ar):
    return sum(ar)

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)