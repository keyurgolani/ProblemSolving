#!/bin/python

import sys


n,k,q = map(int, raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
for a0 in xrange(q):
    m = int(raw_input().strip())
    print a[(m - (k % len(a)))]
