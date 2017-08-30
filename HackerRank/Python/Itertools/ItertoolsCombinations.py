from itertools import combinations
line = raw_input()
line_list = sorted(list(line.split()[0]))
limit = int(line.split()[1])
for size in range(1, limit+1):
    for combination in list(combinations(line_list, size)):
        print ''.join(list(combination))
