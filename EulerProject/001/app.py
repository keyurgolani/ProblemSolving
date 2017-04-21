import sys


def answer(num):
    sum = 0
    for _num in xrange(num):
        # Assuming that multiples of 3 or 5 doesn't mean to exclude multiples of both
        # If otherwise given,
        # instead of "if _num % 3 == 0 or _num % 5 == 0:"
        # you can add "if (_num % 3 == 0 or _num % 5 == 0) and _num % 15 != 0:"
        if _num % 3 == 0 or _num % 5 == 0:
            sum += _num
    return sum


def main():
    idx = 0
    for line in sys.stdin:
        print "Case #{}: {}".format(idx, answer(int(line)))
        idx += 1


if __name__ == '__main__':
    main()
