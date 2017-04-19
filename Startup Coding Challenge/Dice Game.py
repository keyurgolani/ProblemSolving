import sys
sys.setrecursionlimit(10000)
cached_values = {}

def get(i):
    if i not in cached_values.keys():
        cached_values[i] = answer(i)
    return cached_values[i]

def answer(num):
    if num == 0:
        return 1
    elif num == 1:
        return get(0)
    elif num == 2:
        return get(1) + get(0)
    elif num == 3:
        return get(2) + get(1) + get(0)
    elif num == 4:
        return get(3) + get(2) + get(1) + get(0)
    elif num == 5:
        return get(4) + get(3) + get(2) + get(1) + get(0)
    elif num >= 6:
        return get(num - 1) + get(num - 2) + get(num - 3) + get(num - 4) + get(num - 5) + get(num - 6)


print(answer(610))
