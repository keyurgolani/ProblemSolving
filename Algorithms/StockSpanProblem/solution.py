from Stack import Stack


def solution(stock_prices):
    previous_maxima = Stack()
    if len(stock_prices) == 0:
        pass
    previous_maxima.push((-1, stock_prices[0]))
    for idx, stock_price in enumerate(stock_prices):
        while stock_price > previous_maxima.top[1]:
            previous_maxima.pop[1]
        else:
            span = (idx - previous_maxima.top[0])
            previous_maxima.push((idx, stock_price))
            yield span


def main():
    for answer in solution(map(int, raw_input().split(" "))):
        print answer


if __name__ == '__main__':
    main()
