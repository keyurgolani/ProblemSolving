# Formula: Height of water column = Minimum(Tallest Left Hand Bar, Tallest Right Hand Bar) - Current Bar Height
# Total Water that can be held = Sum(Height of water column for all the bars)


def answer(heights):
    # Initialize total_water to 0
    total_water = 0
    # Calculate water gathered over each tower and keep adding it.
    for idx, tower in enumerate(heights):
        # The heighest tower on left side inclusive the current tower.
        left_heighest = max(heights[:idx+1])
        # The heighest tower on right side inclusive the current tower.
        right_heighest = max(heights[idx:])
        # Water gathered over current tower is height of lower of
        # left and right heighest towers minus current tower height.
        total_water += (left_heighest if left_heighest < right_heighest else right_heighest) - tower
    return total_water


def main():
    # Handle each case in loop
    for case in xrange(int(raw_input())):
        # Print the output of "answer" function in required format.
        print 'Case #{}: {}'.format(case+1, answer(map(int, raw_input().split())))


if __name__ == '__main__':
    main()
