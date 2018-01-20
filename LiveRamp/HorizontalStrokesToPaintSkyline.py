def solution(input_array):
    if len(input_array) == 0:
        return 0
    input_array.append(0)
    differences = map(lambda x: x[1] - x[0], zip(input_array[1:], input_array[:-1]))
    positive_differences = filter(lambda x: x >= 0, differences)
    strokes = reduce(lambda x, y: x + y, positive_differences)
    return strokes

def main():
    # input_array = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
    # input_array = []
    # input_array = [1, 1, 1, 1, 1, 1, 1, 1]
    # input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # input_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    input_array = [0, 0, 0, 0, 0, 0, 0]
    print solution(input_array)

if __name__ == '__main__':
    main()