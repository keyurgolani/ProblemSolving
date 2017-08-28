#!/bin/python

import sys


n = float(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print len([x for x in arr if x > 0]) / n
print len([x for x in arr if x < 0]) / n
print len([x for x in arr if x == 0]) / n