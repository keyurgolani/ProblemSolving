def get_hash(value):
    hash_value = 0
    idx = 0
    for char in value:
        hash_value += ord(char) * (101**idx)
        idx += 1
    return hash_value


def recalculate_hash(old_hash=None, remove_char=None, add_char=None, pattern_length=None, value=None):
    if value is not None:
        return get_hash(value)
    else:
        return ((old_hash - ord(remove_char)) / 101) + (ord(add_char) * 101**(pattern_length - 1))


def answer(pattern, string):
    pattern_hash = get_hash(pattern)
    pattern_length = len(pattern)
    current_hash = recalculate_hash(value=string[:pattern_length])
    for idx in range(len(string) - pattern_length):
        if current_hash == pattern_hash:
            if string[idx:idx + pattern_length] == pattern:
                return True
        current_hash = recalculate_hash(current_hash, string[idx], string[idx + 3], pattern_length)
    else:
        if current_hash == pattern_hash:
            if string[idx + 1:idx + pattern_length + 1] == pattern:
                return True
        return False


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, answer(raw_input(), raw_input()))


if __name__ == '__main__':
    main()
