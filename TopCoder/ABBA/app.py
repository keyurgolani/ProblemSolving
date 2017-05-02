def OP1(input):
    return input + 'A'


def OP2(input):
    return input[::-1] + 'B'


def answer(input, target):
    if input == target:
        return 'Possible'
    if input not in target and input[::-1] not in target:
        return 'Impossible'
    if len(input) >= len(target):
        return 'Impossible'
    if answer(OP1(input), target) == 'Possible' or answer(OP2(input), target) == 'Possible':
        return 'Possible'
    else:
        return 'Impossible'


def main():
    for case in range(int(raw_input())):
        input, target = raw_input().split()
        print "Case #{}: {}".format(case, answer(input, target))


if __name__ == '__main__':
    main()
