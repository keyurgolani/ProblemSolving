import datetime

def answer(M, F):
    long_M = long(M)
    long_F = long(F)
    steps = 0
    while long_F != 1 and long_M != 1:
        if long_F == 0 or long_M == 0 or long_F % long_M == 0 or long_M % long_F == 0 or (long_M % 2 == 0 and long_F % 2 == 0):
            return 'impossible'
        else:
            if long_F < long_M:
                increment, long_M = divmod(long_M, long_F)
                steps += increment
            elif long_F > long_M:
                increment, long_F = divmod(long_F, long_M)
                steps += increment
    else:
        steps += abs(long_F - long_M)
    return steps



def main():
    start = datetime.datetime.now()
    print answer(*tuple(raw_input().split()))
    print (datetime.datetime.now() - start).total_seconds()


main()
