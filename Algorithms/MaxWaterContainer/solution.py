def find_max_index(numbers):
	max_index = 0
	for idx in xrange(len(numbers)):
		if numbers[idx] > numbers[max_index]:
			max_index = idx
	return max_index

def solution(heights):
	max_water = (0, 0, 0)
	left_max = 0
	right_max = find_max_index(heights)
	for idx in xrange(1, len(heights)-1):
		if idx == right_max:
			right_max = idx + find_max_index(heights[idx+1:])
		water_on_left = min(heights[left_max], heights[idx]) * (idx - left_max)
		if water_on_left > max_water[2]:
			max_water = (left_max, idx, water_on_left)
		water_on_right = min(heights[left_max], heights[idx]) * (idx - left_max)
		if water_on_right > max_water[2]:
			max_water = (idx, right_max, water_on_left)
		if heights[idx] > heights[left_max]:
			left_max = idx
	return (max_water[0], max_water[1])


def main():
	for _ in xrange(int(raw_input())):
		print "Case #{}: {}".format(_, solution(map(int, raw_input().split())))

if __name__ == '__main__':
	main()