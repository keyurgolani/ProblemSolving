from itertools import product
for result in product(map(int, raw_input().split()), map(int, raw_input().split())):
    print result,
