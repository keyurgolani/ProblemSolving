import sys

def primeOrNot(value):
    if value <= 3:
        return 1
    elif value % 2 == 0:
        return 2
    elif value % 3 == 0:
        return 3
    idx = 5
    while idx * idx < value:
        if value % idx == 0:
            return idx
        elif value % (idx + 2) == 0:
            return idx + 2
        idx += 6
    return 1

def main():
    for value in sys.stdin:
        print primeOrNot(int(value))
    

if __name__ == '__main__':
    main()