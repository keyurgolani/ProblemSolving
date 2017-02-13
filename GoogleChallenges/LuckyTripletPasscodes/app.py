def answer(l):
	return len([(x[1], y[1], z[1]) for x in enumerate(l) for y in enumerate(l) if x[0] < y[0] and y[1] % x[1] == 0 for z in enumerate(l) if y[0] < z[0] and z[1] % y[1] == 0])


def main():
	print answer(map(int, raw_input().split()))


main()
