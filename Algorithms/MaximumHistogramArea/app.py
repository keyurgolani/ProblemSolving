from Stack import Stack


def answer(histogram):
    positions = Stack()
    heights = Stack()
    max_rectangle = -1
    for idx in range(len(histogram)):
        if histogram[idx] > heights.top or idx == 0:
            positions.push(idx)
            heights.push(histogram[idx])
        elif histogram[idx] < heights.top:
            latest_height = None
            while heights.top is not None and histogram[idx] < heights.top:
                max_rectangle = pop_and_calculate_rectangle(idx, positions, heights, max_rectangle)
                latest_position = positions.pop
                latest_height = heights.pop
            positions.push(latest_height)
            heights.push(histogram[idx])
    while heights.top is not None and positions.top is not None:
        max_rectangle = pop_and_calculate_rectangle(len(histogram), positions, heights, max_rectangle)
        heights.pop
        positions.pop
    return max_rectangle


def pop_and_calculate_rectangle(idx, positions, heights, max_rectangle):
    rectangle = heights.top * (idx - positions.top)
    if rectangle > max_rectangle:
        return rectangle
    else:
        return max_rectangle


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, answer(map(int, raw_input().split())))


if __name__ == '__main__':
    main()
