def answer(start, length):
    result = 0
    if start % 2 == 0:
        for i in xrange(length, 0, -1):
            if i % 4 == 1:
                result ^= ((length**2) - i * (length - 1) - 1 + start)
            elif i % 4 == 2:
                if length % 2 == 0:
                    result ^= 1
                else:
                    result ^= ((length**2) - i * (length - 1) - 1 + start) ^ ((length - i) * length + start)
            elif i % 4 == 3:
                result ^= ((length**2) - i * (length - 1) - 1 + start) ^ 1
            else:
                if length % 2 == 1:
                    result ^= ((length**2) - i * (length - 1) - 1 + start) ^ ((length - i) * length + start) ^ 1
    else:
        for i in xrange(length, 0, -1):
            if i % 4 == 1:
                result ^= ((length - i) * length + start)
            elif i % 4 == 2:
                if length % 2 == 1:
                    result ^= 1
                else:
                    result ^= ((length**2) - i * (length - 1) - 1 + start) ^ ((length - i) * length + start)
            elif i % 4 == 3:
                result ^= ((length - i) * length + start) ^ 1
            else:
                if length % 2 == 0:
                    result ^= ((length**2) - i * (length - 1) - 1 + start) ^ ((length - i) * length + start) ^ 1
    return result


def main():
    print answer(*tuple(map(int, raw_input().split())))


main()
