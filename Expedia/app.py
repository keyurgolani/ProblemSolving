def solution(values):
    frequency = {}
    for value in values:
        if value in frequency.keys():
            frequency[value] += 1
        else:
            frequency[value] = 1
    return sorted(values, key=lambda x: (frequency[x], x))


def main():
    values = []
    for _ in xrange(int(raw_input())):
        values.append(int(raw_input()))
    for sorted_value in solution(values):
        print sorted_value


if __name__ == '__main__':
    main()
