#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
max = arr[0]
min = arr[0]
total = 0
for value in arr:
    total += value
    if value < min:
        min = value
    if value > max:
        max = value
print total - max, total - min