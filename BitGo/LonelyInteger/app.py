def lonelyInt(values):
    ans = 0
    for value in values:
        ans ^= value
    return ans

def main():
    values = map(int, raw_input().split(" "))
    print lonelyInt(values)

if __name__ == '__main__':
    main()