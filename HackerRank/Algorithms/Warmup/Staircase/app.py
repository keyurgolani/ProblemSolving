#!/bin/python

import sys


n = int(raw_input().strip())
for element in [n + 1 for n in xrange(n)]:
    print ' ' * (n - element + 1) + '#' * element