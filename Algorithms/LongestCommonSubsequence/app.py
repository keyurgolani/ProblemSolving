cache_store = {}
cache_store2 = {}


def LCS(A1, A2):
    if (A1, A2) not in cache_store.keys():
        if len(A1) == 0 or len(A2) == 0:
            cache_store[(A1, A2)] = []
        elif A1[-1] == A2[-1]:
            cache_store[(A1, A2)] = LCS(A1[:-1], A2[:-1]) + [A1[-1]]
        else:
            one = LCS(A1[:-1], A2)
            two = LCS(A1, A2[:-1])
            if len(one) > len(two):
                cache_store[(A1, A2)] = one
            else:
                cache_store[(A1, A2)] = two
    return cache_store[(A1, A2)]


def LCS2(A1, A2):
    if (A1, A2) not in cache_store2.keys():
        if len(A1) == 0 or len(A2) == 0:
            cache_store2[(A1, A2)] = 0
        elif A1[-1] == A2[-1]:
            cache_store2[(A1, A2)] = LCS2(A1[:-1], A2[:-1]) + 1
        else:
            one = LCS2(A1[:-1], A2)
            two = LCS2(A1, A2[:-1])
            cache_store2[(A1, A2)] = one if one > two else two
    return cache_store2[(A1, A2)]


def main():
    for _ in range(int(raw_input())):
        input1 = raw_input()
        input2 = raw_input()
        print "Case {}: {}".format(_, LCS(input1, input2))
        print "Case {}: {}".format(_, LCS2(input1, input2))


if __name__ == '__main__':
    main()
