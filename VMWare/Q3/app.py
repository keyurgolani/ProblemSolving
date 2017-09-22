def solution(m, a):
    minDistance = 0
    for idx in xrange(len(m)):
        for f, t in zip(str(m[idx]), str(a[idx])):
            minDistance += abs(int(f) - int(t))
    return minDistance

def main():
    m = []
    m_count = int(raw_input())
    for _ in xrange(m_count):
        m.append(int(raw_input()))
    a = []
    a_count = int(raw_input())
    for _ in xrange(a_count):
        a.append(int(raw_input()))
    print solution(m, a)


main()