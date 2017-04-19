def answer(prices, tax):
    total_profit = 0
    current_idx = 0
    while current_idx < len(prices):
        buy_price = prices[current_idx]
        # print buy_price
        next_max = max(prices[current_idx:])
        # print next_max
        if buy_price == next_max:
            current_idx += 1
        elif next_max - buy_price - tax >= 0:
            total_profit += next_max - buy_price - tax
            current_idx = prices.index(next_max) + 1
    return total_profit



def main():
    for case in range(int(raw_input())):
        print(answer(map(int, raw_input().split()), int(raw_input())))


if __name__ == '__main__':
    main()
