def LCS(A1, A2):
    if len(A1) == 0 or len(A2) == 0:
        return []
    if A1[-1] == A2[-1]:
        return LCS(A1[:-1], A2[:-1]) + [A1[-1]]
    else:
        one = LCS(A1[:-1], A2)
        two = LCS(A1, A2[:-1])
        if len(one) > len(two):
            return one
        else:
            return two


def LCS2(A1, A2):
    if len(A1) == 0 or len(A2) == 0:
        return 0
    if A1[-1] == A2[-1]:
        return LCS2(A1[:-1], A2[:-1]) + 1
    else:
        one = LCS2(A1[:-1], A2)
        two = LCS2(A1, A2[:-1])
        return one if one > two else two


def main():
    for _ in range(int(raw_input())):
        input1 = raw_input()
        input2 = raw_input()
        print "Case {}: {}".format(_, LCS(input1, input2))
        print "Case {}: {}".format(_, LCS2(input1, input2))


if __name__ == '__main__':
    main()
