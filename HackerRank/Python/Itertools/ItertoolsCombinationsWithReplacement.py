from itertools import combinations_with_replacement
line = raw_input()
line_list = sorted(list(line.split()[0]))
size = int(line.split()[1])
for combination in combinations_with_replacement(line_list, size):
    print ''.join(list(combination))
