def solution(target, values):
	values_dict = {}
	for idx in xrange(len(values)):
		try:
			idx_two = values_dict[target - values[idx]]
		except KeyError:
			values_dict[values[idx]] = idx
			continue
		else:
			return (idx_two, idx)
	return -1


def solution2(target, values):
	sorted_values = sorted(values)
	start, end = 0, len(values) - 1
	while start != end:
		if sorted_values[start] + sorted_values[end] == target:
			return (values.index(sorted_values[start]), values.index(sorted_values[end]))
		elif sorted_values[start] + sorted_values[end] < target:
			start += 1
		else:
			end -= 1
	return -1

def main():
	for _ in xrange(int(raw_input())):
		print "Case #{}: {}".format(_, solution(int(raw_input()), map(int, raw_input().split())))

if __name__ == '__main__':
	main()