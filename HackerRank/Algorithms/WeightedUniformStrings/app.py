#!/bin/python

import sys


s = raw_input().strip()
n = int(raw_input().strip())
possible_totals = set()
current_char = None
current_char_count = 0
for char in s:
    if char == current_char:
        current_char_count += 1
    else:
        if current_char is not None:
            for count in xrange(current_char_count):
                possible_totals.add((ord(current_char) - 96) * (count + 1))
        current_char = char
        current_char_count = 1
for count in xrange(current_char_count):
    possible_totals.add((ord(char) - 96) * (count + 1))
for a0 in xrange(n):
    x = int(raw_input().strip())
    print "YES" if x in possible_totals else "NO"
