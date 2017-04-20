cached_results = {}
cached_results2 = {}


def knapsack(values, weights, capacity):
    if (len(values), capacity) not in cached_results.keys():
        if len(values) == 0 or capacity == 0:
            cached_results[(len(values), capacity)] = 0
        elif len(values) == 1 and capacity >= weights[0]:
            cached_results[(len(values), capacity)] = values[0]
        else:
            if capacity >= weights[0]:
                with_current = knapsack(values[1:], weights[1:], capacity - weights[0]) + values[0]
                without_current = knapsack(values[1:], weights[1:], capacity)
                cached_results[(len(values), capacity)] = with_current if with_current > without_current else without_current
            else:
                cached_results[(len(values), capacity)] = knapsack(values[1:], weights[1:], capacity)
    return cached_results[(len(values), capacity)]


def knapsack2(values, weights, capacity):
    if (len(values), capacity) not in cached_results2.keys():
        if len(values) == 0 or capacity == 0:
            cached_results2[(len(values), capacity)] = []
        elif len(values) == 1 and capacity >= weights[0]:
            cached_results2[(len(values), capacity)] = values
        else:
            if capacity >= weights[0]:
                with_current = knapsack2(values[1:], weights[1:], capacity - weights[0]) + values[:1]
                without_current = knapsack2(values[1:], weights[1:], capacity)
                cached_results2[(len(values), capacity)] = with_current if sum(with_current) > sum(without_current) else without_current
            else:
                cached_results2[(len(values), capacity)] = knapsack2(values[1:], weights[1:], capacity)
    return cached_results2[(len(values), capacity)]


def main():
    for _ in range(int(raw_input())):
        values = map(int, raw_input().split())
        weights = map(int, raw_input().split())
        capacity = int(raw_input())
        print "Case {}: {}".format(_, knapsack(values, weights, capacity))
        print "Case {}: {}".format(_, knapsack2(values, weights, capacity))


if __name__ == '__main__':
    main()
