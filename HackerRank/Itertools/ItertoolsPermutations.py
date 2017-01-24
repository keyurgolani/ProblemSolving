from itertools import permutations
line, size = raw_input().split()
size = int(size)
for substring in sorted(permutations(line, size)):
    print ''.join(substring)
