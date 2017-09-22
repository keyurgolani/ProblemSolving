import sys

def solution(values):
    return sorted(values, key=lambda x: (bin(x)[2:].count('1'), x))


def main():
    _ = raw_input()
    values = []
    for line in sys.stdin:
        values.append(int(line))
    print solution(values)


if __name__ == "__main__":
    main()
