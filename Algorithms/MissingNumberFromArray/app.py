import sys


def answer(_p):
    current_sum = sum(_p)
    length = len(_p)
    total = (length + 1) * (length + 2) / 2
    return total - current_sum


def main():
    case = 0
    for line in sys.stdin:
        print "Case #{}: {}".format(case, answer(map(int, line.split())))
        case += 1


if __name__ == '__main__':
    main()
