n = input()
s = set(map(int, raw_input().split()))
N = input()
for _ in range(N):
    command_line = raw_input()
    command = command_line.split()
    if command[0] == 'pop':
        try:
            s.pop()
        except KeyError:
            pass
    elif command[0] == 'remove':
        try:
            s.remove(int(command[1]))
        except KeyError:
            pass
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    else:
        pass

print sum(s)
