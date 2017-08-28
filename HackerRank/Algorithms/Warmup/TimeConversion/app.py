#!/bin/python

import sys


time = raw_input().strip()
hms = time[:8].split(':')
if time[-2:] == 'PM':
    print str((int(hms[0]) % 12) + 12).zfill(2) + ':' + hms[1] + ':' + hms[2]
else:
    print str(int(hms[0]) % 12).zfill(2) + ':' + hms[1] + ':' + hms[2]
