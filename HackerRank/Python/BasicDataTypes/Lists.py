if __name__ == '__main__':
    N = int(raw_input())
    l1 = []
    for num in range(N):
        command = raw_input()
        if command.split()[0] == 'insert':
            l1.insert(int(command.split()[1]), int(command.split()[2]))
        elif command.split()[0] == 'print':
            print l1
        elif command.split()[0] == 'remove':
            l1.remove(int(command.split()[1]))
        elif command.split()[0] == 'append':
            l1.append(int(command.split()[1]))
        elif command.split()[0] == 'sort':
            l1.sort()
        elif command.split()[0] == 'pop':
            l1.pop()
        elif command.split()[0] == 'reverse':
            l1.reverse()
        else:
            pass
