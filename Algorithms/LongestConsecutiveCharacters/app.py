def longest_consecutive_character(sequence):
    current_char = None
    current_count = 0
    max_char = None
    max_count = 0
    prev_char = None
    for char in sequence:
        if char == prev_char:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_char = current_char
            prev_char = char
            current_char = char
            current_count = 1
    return {max_char: max_count}


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, longest_consecutive_character(raw_input()))


if __name__ == '__main__':
    main()
