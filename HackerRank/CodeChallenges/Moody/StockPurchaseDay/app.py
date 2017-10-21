#!/usr/bin/env python2
import sys

def main():
    days = int(raw_input())
    stock_prices = map(int, raw_input().split(" "))
    queries = int(raw_input())
    for query in sys.stdin:
        for day in range(days)[::-1]:
            if int(query) == stock_prices[day]:
                print day + 1
                break
        else:
            print -1


if __name__ == '__main__':
    main()
