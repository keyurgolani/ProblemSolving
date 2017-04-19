def answer(str1, str2):
    result_str = ""
    idx = 0
    for char1, char2 in zip(str1, str2):
        result_str += char1
        result_str += char2
        idx += 1
    if len(str1) > idx:
        result_str += str1[idx:]
    if len(str2) > idx:
        result_str += str2[idx:]
    return result_str


def main():
    print answer(raw_input(), raw_input())


if __name__ == '__main__':
    main()
