from itertools import groupby
line = raw_input()
for compression in groupby(list(line)):
    print (len(list(compression[1])), int(compression[0])),
