import datetime
from itertools import groupby

def answer(l):
    answer = []
    for key1, group1 in groupby(sorted(l, key=lambda s: int(s.split('.')[0])), key=lambda s: int(s.split('.')[0])):
        for key2, group2 in groupby(sorted(group1, key=lambda s: int(s.split('.')[1]) if s.count('.') > 0 else -1), key=lambda s: int(s.split('.')[1]) if s.count('.') > 0 else -1):
            for key3, group3 in groupby(sorted(group2, key=lambda s: int(s.split('.')[2]) if s.count('.') > 1 else -1), key=lambda s: int(s.split('.')[2]) if s.count('.') > 1 else -1):
                for element3 in group3:
                    answer.append(element3)
    return answer



def main():
    print answer(raw_input().split())


main()
