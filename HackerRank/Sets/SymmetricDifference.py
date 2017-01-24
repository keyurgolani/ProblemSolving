set1_count = int(raw_input())
set1 = set(map(int, raw_input().split()))
set2_count = int(raw_input())
set2 = set(map(int, raw_input().split()))
for element in sorted(list(set1 ^ set2)):
    print element
