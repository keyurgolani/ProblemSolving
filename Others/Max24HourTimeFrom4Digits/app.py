l = map(int, raw_input().split())
time = [0, 0, 0, 0]
remaining = l
if 2 in l:
    remaining.remove(2)
    if 3 in remaining:
        time[0] = 2
        time[1] = 3
        remaining.remove(3)
    elif 2 in remaining:
        time[0] = 2
        time[1] = 2
        remaining.remove(2)
    elif 1 in remaining:
        time[0] = 2
        time[1] = 1
        remaining.remove(1)
    elif 0 in remaining:
        time[0] = 2
        time[1] = 0
        remaining.remove(0)
elif 1 in l:
    time[0] = 1
    remaining.remove(1)
    time[1] = max(remaining)
    remaining.remove(time[1])
elif 0 in l:
    time[0] = 0
    remaining.remove(0)
    time[1] = max(remaining)
    remaining.remove(time[1])
else:
    print 'NOT POSSIBLE'
    exit()
next_max = max(remaining)
next_min = min(remaining)
if next_max < 6 and next_min > 0:
    time[2] = next_max
    remaining.remove(next_max)
    time[3] = max(remaining)
elif next_min < 6:
    time[3] = next_max
    remaining.remove(next_max)
    time[2] = max(remaining)
else:
    print 'NOT POSSIBLE'
    exit()


print str(time[0]) + str(time[1]) + ':' + str(time[2]) + str(time[3])
