def answer(in_string):
    start = 0
    end = len(in_string) - 1
    while start < end:
        while in_string[start] == 0:
            start += 1
        while in_string[end] == 1:
            end -= 1
        if start < end:
            in_string[start], in_string[end] = in_string[end], in_string[start]
    return in_string


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, ''.join(map(str, answer(map(int, raw_input())))))


if __name__ == '__main__':
    main()
