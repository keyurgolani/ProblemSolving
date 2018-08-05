import sys

def Solution(count):
    half = count / 2
    answer = range(-half, half+1)
    if count % 2 == 0:
        answer.remove(0)
    return answer

def Solution2(count, target):
    half = count / 2
    offset = float(target) / count
    answer = range(-half, half+1)
    if count % 2 == 0:
        answer.remove(0)
    return [element + offset for element in answer]
    

def main():
    for line in sys.stdin:
        count, target = map(int, line.split(' '))
        print Solution(count)
        print Solution2(count, target)


if __name__ == '__main__':
    main()


