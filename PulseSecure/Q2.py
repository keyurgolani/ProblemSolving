# Enter your code here. Read input from STDIN. Print output to STDOUT
l, m = map(int, raw_input().split())
l = [0]*l
for _ in xrange(m):
    range_start, range_end, num = map(int, raw_input().split())
    range_start -= 1
    range_end -= 1
    l = l[:range_start] + [x+num for x in l[range_start:range_end+1]] + l[range_end+1:]
print max(l)
