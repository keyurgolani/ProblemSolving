#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
diff = 0
for i in xrange(n):
    diff = diff + (a[i][i] - a[i][n-i-1])
print diff if diff > 0 else -diff
