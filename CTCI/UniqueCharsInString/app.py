def answer(string):
    if len(string) > 256:
        return False
    present = [False] * 256
    for char in string:
        idx = ord(char)
        if present[idx] is True:
            return False
        else:
            present[idx] = True
    return True


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, answer(raw_input()))


if __name__ == '__main__':
    main()
