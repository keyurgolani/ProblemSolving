from collections import Counter
K = int(input())
count_dict = Counter(raw_input().split())
print {v: k for k, v in count_dict.items()}[1]
