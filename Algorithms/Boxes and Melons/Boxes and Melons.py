def solution(boxes, melons):
    mat = []
    for _ in range(len(melons)):
        mat.append([0]*len(boxes))
    for idx, row in enumerate(mat):
        current_melon = melons[idx]
        for jdx, element in enumerate(row):
            current_box = boxes[jdx]
            if current_melon <= current_box:
                mat[idx][jdx] = 1
    max_len = 0
    current_len = 0
    for idx in range(len(mat)):
        jdx = 0
        while idx < len(mat) and jdx < len(mat[0]):
            if mat[idx][jdx] == 1:
                idx += 1
                jdx += 1
                current_len += 1
            else:
                jdx += 1
        if current_len > max_len:
            max_len = current_len
        current_len = 0
    for jdx in range(len(mat[0])):
        idx = 0
        while idx < len(mat) and jdx < len(mat[0]):
            if mat[idx][jdx] == 1:
                idx += 1
                jdx += 1
                current_len += 1
            else:
                jdx += 1
        if current_len > max_len:
            max_len = current_len
        current_len = 0
    return max_len

def main():
    print solution([1, 2, 1, 1], [3, 2, 1])

if __name__ == '__main__':
    main()