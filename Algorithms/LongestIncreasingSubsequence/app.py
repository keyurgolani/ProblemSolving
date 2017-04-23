import math


def answer(arr):
    longest_subsequence = []
    for element in arr:
        if len(longest_subsequence) == 0 or longest_subsequence[-1] < element:
            longest_subsequence.append(element)
        else:
            start = 0
            end = len(longest_subsequence) - 1
            if len(longest_subsequence) > 2:
                while end - start > 1:
                    mid_idx = int(math.ceil((end + start) / 2))
                    if longest_subsequence[mid_idx] > element:
                        end = mid_idx
                    else:
                        start = mid_idx
            else:
                for idx in range(len(longest_subsequence)):
                    if element < longest_subsequence[idx]:
                        start = idx - 1
                        break
            longest_subsequence = longest_subsequence[:start + 1] + [element]
    return longest_subsequence


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, answer(map(int, raw_input().split())))


if __name__ == '__main__':
    main()
