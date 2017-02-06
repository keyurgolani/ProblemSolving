def answer(M, F):
    long_M = long(M)
    long_F = long(F)
    steps = 0
    while not long_F == long_M == 1:
        if long_F == 0 or long_M == 0:
            return 'impossible'
        else:
            if long_F < long_M:
                long_M = long_M - long_F
                steps += 1
            elif long_F > long_M:
                long_F = long_F - long_M
                steps += 1
            else:
                return 'impossible'
    return steps



def main():
    print answer(*tuple(raw_input().split()))


main()
