def answer(s):
    indexes = [i for i, ltr in enumerate(s) if ltr == s[0]]
    for index in indexes[1:]:
        count = s.count(s[:index])
        if count * len(s[:index]) == len(s):
            return count
    else:
        return 1


def main():
    print answer(raw_input())


main()
