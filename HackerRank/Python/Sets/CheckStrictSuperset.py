A = set(raw_input().split())
N = int(input())
print_value = True
for _ in range(N):
    subset = set(raw_input().split())
    if len(subset - A) != 0 or len(A - subset) == 0:
        print_value = False
        break
print print_value
