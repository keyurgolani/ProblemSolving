def count_negatives(m):
    negatives = 0
    row = 1
    col = len(m[0])
    while row != len(m) or col != 0:
        if m[row - 1][col - 1] < 0:
            negatives += col
            row += 1
        else:
            col -= 1
    return negatives


def main():
    for case in range(int(raw_input())):
        rows, cols = map(int, raw_input().split())
        m = []
        for row in range(rows):
            m.append(map(int, raw_input().split()))
        print "Case #{}: {}".format(case, count_negatives(m))


if __name__ == '__main__':
    main()
