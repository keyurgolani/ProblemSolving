happiness = 0
n, m = map(int, raw_input().split())
arr = list(map(int, raw_input().split()))
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))
for element in arr:
    if element in A:
        happiness += 1
    elif element in B:
        happiness -= 1
print happiness
