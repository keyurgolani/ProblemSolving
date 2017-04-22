import sys


# Specific Solution
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


# More time complexity but a more generic solution
def answer2(num, base_values, multiple_of_all=False):
    sum = 0
    for _num in xrange(num):
        multiples_of = 0
        for base_value in base_values:
            if _num % base_value == 0:
                multiples_of += 1
                if multiple_of_all:
                    break
        if multiples_of == 1:
            sum += _num
    return sum


def main():
    idx = 0
    for line in sys.stdin:
        print "Case #{}: {}".format(idx, answer(int(line)))
        print "Case #{}: {}".format(idx, answer2(int(line), [3, 5], multiple_of_all=True))
        idx += 1


if __name__ == '__main__':
    main()
