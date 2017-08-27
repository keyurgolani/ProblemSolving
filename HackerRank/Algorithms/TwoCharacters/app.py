#!/bin/python

import sys


s_len = int(raw_input().strip())
s = raw_input().strip()

chars = {}

def validate(s, char1, char2):
    length = 0
    previous_char = None
    for char in s:
        if char in (char1, char2):
            if previous_char != None and previous_char == char:
                return 0
            else:
                previous_char = char
                length += 1
    return length


for char in s:
    try:
        chars[char] += 1
    except KeyError:
        chars[char] = 1
chars_list = sorted(chars.items(), key=lambda x: x[1], reverse=True)
max_len = 0
for idx in xrange(len(chars_list) - 1):
    for idy in xrange(idx+1, len(chars_list)):
        if chars_list[idx][1] - chars_list[idy][1] <= 1:
            current_len = validate(s, chars_list[idx][0], chars_list[idy][0])
            if current_len > max_len:
                max_len = current_len
print max_len
    
