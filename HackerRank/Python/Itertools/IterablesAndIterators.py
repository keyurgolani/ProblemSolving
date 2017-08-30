from itertools import combinations
n = int(raw_input())
char_list = raw_input().split()
size = int(raw_input())
combination_list = list(combinations(char_list, size))
print len([x for x in combination_list if 'a' in list(x)]) / float(len(combination_list))
