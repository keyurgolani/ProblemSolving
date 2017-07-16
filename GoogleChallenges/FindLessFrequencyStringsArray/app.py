def frequency_of(input_string):
    return input_string.count(reduce(lambda x, y: x if x < y else y, input_string))

def solution(A, B):
    return map(lambda B_string: sum(map(lambda A_string: 1 if frequency_of(B_string) > frequency_of(A_string) else 0, A)), B)


def main():
    for case in range(int(raw_input())):
        A = raw_input().split(" ")
        B = raw_input().split(" ")
        print "Case #{}: {}".format(case, solution(A, B))


if __name__ == '__main__':
    main()
