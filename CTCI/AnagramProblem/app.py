def index_agnostic_hash(value):
    return reduce(lambda x, y: x + y, map(lambda x: ord(x), value))


def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    elif index_agnostic_hash(str1) != index_agnostic_hash(str2):
        return False
    elif sorted(str1) != sorted(str2):
        return False
    else:
        return True


def main():
    for case in range(int(raw_input())):
        str1, str2 = raw_input().split()
        print "Case #{}: {}".format(case, is_anagram(str1, str2))


if __name__ == '__main__':
    main()
