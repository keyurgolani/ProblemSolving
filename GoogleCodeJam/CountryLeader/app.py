def answer(names):
    return reduce(lambda a, b: a if a[0] > b[0] else b if b[0] > a[0] else a if a[1] < b[1] else b, map(lambda x: (len(set(x) - set(' ')), x), names))


def main():
    T = int(raw_input())
    for _ in range(T):
        N = int(raw_input())
        names = []
        for n in range(N):
            names.append(raw_input().strip())
        print 'Case #{}: {}'.format(_+1, answer(names)[1])


main()
