import sys


def answer(num, filter=0):
    sum = 0
    current_values = [0, 1]
    while current_values[0] < num:
        if filter == 0 or (filter == 1 and current_values[0] % 2 == 1) or (filter == 2 and current_values[0] % 2 == 0):
            sum += current_values[0]
        current_values = [current_values[1], current_values[0] + current_values[1]]
    return sum


def main():
    idx = 0
    for line in sys.stdin:
        # Filter 0 = All, 1 = Include only Odd, 2 = Include only Even
        print "Case #{}: {}".format(idx, answer(int(line), filter=1))
        idx += 1


if __name__ == '__main__':
    main()
