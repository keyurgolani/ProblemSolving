import itertools

def Max24HourTimeFrom4Digits(*args):
    h = -1
    m = -1
    for permutation in list(itertools.permutations(args)):
        hours = (permutation[0] * 10) + permutation[1]
        minutes = (permutation[2] * 10) + permutation[3]
        if hours < 24 and minutes < 60:
            if hours > h or (hours == h and minutes > m):
                h = hours
                m = minutes
    if h != -1 and m != -1:
        return str(h).zfill(2) + ':' + str(m).zfill(2)
    else:
        return 'NOT POSSIBLE'


def main():
    l = map(int, raw_input().split())
    print Max24HourTimeFrom4Digits(l[0], l[1], l[2], l[3])


main()
