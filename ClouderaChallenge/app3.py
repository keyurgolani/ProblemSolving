def answer(in_num):
    n = in_num
    current_power = 0
    compliment = 0
    while n > 1:
        n, remainder = divmod(n, 2)
        remainder = 1 if remainder == 0 else 0
        compliment += (remainder * (2**current_power))
        current_power += 1
    return compliment


def main():
    print answer(int(raw_input()))


if __name__ == '__main__':
    main()
