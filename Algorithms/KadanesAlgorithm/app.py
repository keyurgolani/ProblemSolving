def max_subarray_sum(A):
    global_max = A[0]
    current_max = A[0]
    for idx in range(1, len(A)):
        current_max = A[idx] if A[idx] > A[idx] + current_max else A[idx] + current_max
        if current_max > global_max:
            global_max = current_max
    return global_max


def max_subarray(A):
    global_max = A[:1]
    current_max = A[:1]
    for idx in range(1, len(A)):
        if A[idx] > A[idx] + sum(current_max):
            current_max = A[idx:idx + 1]
        else:
            current_max += A[idx:idx + 1]
        if sum(current_max) > sum(global_max):
            global_max = current_max[:]
    return global_max


def main():
    for _ in range(int(raw_input())):
        A = map(int, raw_input().split())
        print "Case #{}  :  {}\t->\t{}".format(str(_ + 1).zfill(2), max_subarray_sum(A), max_subarray(A))


if __name__ == '__main__':
    main()
