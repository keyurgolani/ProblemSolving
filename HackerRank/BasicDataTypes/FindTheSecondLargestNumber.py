if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    largest = arr[-1]
    while True:
        try:
            arr.remove(largest)
        except ValueError:
            break
    print arr[-1]
