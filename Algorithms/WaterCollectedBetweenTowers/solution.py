# Formula: Height of water column = Minimum(Tallest Left Hand Bar, Tallest Right Hand Bar) - Current Bar Height
# Total Water that can be held = Sum(Height of water column for all the bars)

# Takes O(n^2) time complexity and no space complexity
def answer(heights):
    # Initialize total_water to 0
    total_water = 0
    # Calculate water gathered over each tower and keep adding it.
    for idx, tower in enumerate(heights):
        # The heighest tower on left side inclusive the current tower.
        left_heighest = max(heights[:idx + 1])
        # The heighest tower on right side inclusive the current tower.
        right_heighest = max(heights[idx:])
        # Water gathered over current tower is height of lower of
        # left and right heighest towers minus current tower height.
        total_water += (left_heighest if left_heighest < right_heighest else right_heighest) - tower
    return total_water


# Takes O(n) time complexity and O(n) space complexity
def answer2(heights):
    local_left_max = []
    current_max = -1
    length = len(heights)
    for idx in xrange(length):
        local_left_max.append(current_max)
        if heights[idx] > current_max:
            current_max = heights[idx]
    local_right_max = []
    current_max = -1
    for idx in range(length)[::-1]:
        local_right_max = [current_max] + local_right_max
        if heights[idx] > current_max:
            current_max = heights[idx]
    water_held = 0
    for idx in range(length):
        current_water_held = min(local_right_max[idx], local_left_max[idx]) - heights[idx]
        water_held += current_water_held if current_water_held > 0 else 0
    return water_held


def main():
    # Handle each case in loop
    for case in xrange(int(raw_input())):
        input_values = map(int, raw_input().split())
        # Print the output of "answer" function in required format.
        print 'Case #{}: {}'.format(case + 1, answer(input_values))
        print 'Case #{}: {}'.format(case + 1, answer2(input_values))


if __name__ == '__main__':
    main()
