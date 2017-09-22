def solution(values, target):
    potential_dict = {}
    count = 0
    for value in values:
        potential_dict[value] = (value - target, value + target)
    for key, val in potential_dict.items():
        if val[0] in potential_dict.keys():
            count += 1
        if val[1] in potential_dict.keys():
            count += 1
    return count / 2


def main():
    _ = int(raw_input())
    values = []
    for idx in range(_):
        values.append(int(raw_input()))
    target = int(raw_input())
    print solution(values, target)


if __name__ == '__main__':
    main()
