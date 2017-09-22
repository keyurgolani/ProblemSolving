def solution(m, n):
    print (n - 1) * (m - 1) * ((m * n) - (n - 1) - (m - 1) - 1) * 3
    if m > n:
        return solution(n, m)
    else:
        current = [1] * m
        for idx in xrange(1, n):
            for jdx in xrange(1, m):
                current[jdx] += current[jdx - 1]
        return current[m - 1]

print solution(*map(int, raw_input().split(" ")))