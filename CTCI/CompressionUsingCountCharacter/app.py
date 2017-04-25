def compress(string):
    output = ""
    buffer = None
    count = 1
    for char in string:
        if buffer is None:
            buffer = char
            output += char
        else:
            if char == buffer:
                count += 1
            else:
                output += str(count)
                count = 1
                output += char
                buffer = char
    if len(output) < len(string):
        return output
    else:
        return string


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, compress(raw_input()))


if __name__ == '__main__':
    main()
