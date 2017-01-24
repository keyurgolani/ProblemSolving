n = input()
s = set(map(int, raw_input().split()))
N = int(input())
for _ in range(N):
    command_line = raw_input()
    command = command_line.split()
    if command[0] == 'intersection_update':
        s &= set(map(int, raw_input().split()))
    elif command[0] == 'update':
        s |= set(map(int, raw_input().split()))
    elif command[0] == 'symmetric_difference_update':
        s ^= set(map(int, raw_input().split()))
    elif command[0] == 'difference_update':
        s -= set(map(int, raw_input().split()))
    else:
        pass
print sum(s)
