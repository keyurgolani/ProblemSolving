mapping = {0: [' '],
1: [''],
2: ['a', 'b', 'c'],
3: ['d', 'e', 'f'],
4: ['g', 'h', 'i'],
5: ['j', 'k', 'l'],
6: ['m', 'n', 'o'],
7: ['p', 'q', 'r', 's'],
8: ['t', 'u', 'v'],
9: ['w', 'x', 'y', 'z']
}

def answer(val1, val2):
    return [(x, y) for x in mapping[val1] for y in mapping[val2]]


def main():
    print answer(*tuple(map(int, raw_input().split())))


main()
