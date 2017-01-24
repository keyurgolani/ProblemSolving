from itertools import product
K, M = map(int, raw_input().split())
inputs = []
for _ in range(K):
    inputs.append(map(int, raw_input().split()[1:]))
inputs_tuple = tuple(inputs)
print max(map(lambda combination : sum([x**2 for x in list(combination)]) % M, product(*inputs_tuple)))
