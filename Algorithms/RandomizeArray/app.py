import random


def randomize(arr):
    for idx in range(1, len(arr) - 1)[::-1]:
        swap_idx = random.randint(0, idx - 1)
        arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
    return arr


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, randomize(map(int, raw_input().split())))


if __name__ == '__main__':
    main()
