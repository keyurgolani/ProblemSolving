import time

def solution(A, K):
    eligible_indexes = range(0, len(A)-K+1)
    current_sub_index = 0
    while current_sub_index < K or (len(eligible_indexes) > 1):
        new_eligible_indexes = []
        current_max = -35565
        for idx in eligible_indexes:
            if A[idx + current_sub_index] > current_max:
                current_max = A[idx+current_sub_index]
        for idx2 in eligible_indexes:
            if A[idx2+current_sub_index] == current_max:
                new_eligible_indexes.append(idx2)
        current_sub_index += 1
        eligible_indexes = new_eligible_indexes
    else:
        if current_sub_index == K and len(eligible_indexes) > 1:
            return None
        else:
            return A[eligible_indexes[0]:eligible_indexes[0]+K]

def main():
    for case in range(int(raw_input())):
        A = map(int, raw_input().split(" "))
        K = int(raw_input())
        print "Case #{}: {}".format(case, solution(A, K))


if __name__ == '__main__':
    main()
