import sys
from Stack import Stack


def answer(mat):
    potential_celebrities = Stack()
    for idx in range(len(mat)):
        if mat[0][idx] == 1:
            potential_celebrities.push(idx)
    while potential_celebrities.top is not None:
        potential_celebrity = potential_celebrities.pop
        for idx in range(len(mat)):
            if mat[idx][potential_celebrity] != 1 and idx != potential_celebrity:
                break
        else:
            return potential_celebrity
    return None


def main():
    mat = []
    for line in sys.stdin:
        mat.append(map(int, line.split()))
    print "Celebrity is person with ID {}".format(answer(mat))


if __name__ == '__main__':
    main()
