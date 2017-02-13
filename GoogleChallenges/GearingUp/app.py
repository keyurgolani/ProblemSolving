def answer(pegs):
	last = pegs[-1]
	first = pegs[0]
	negatives = [2 * x for x in pegs[-2::-2]]
	positives = [2 * x for x in pegs[-3::-2]]
	a = last + sum(positives) - sum(negatives)
	b = 1
	if len(pegs) % 2 == 0:
		a = 2 * (a + first)
		b = 3
		if a % 3 == 0:
			a = a / 3
			b = 1
	else:
		a = - 2 * (a - first)
	radiuses = []
	radiuses.append(a / b)
	for idx, peg in enumerate(pegs[1:]):
		radius = peg - pegs[idx] - radiuses[-1]
		if radius <= 0:
			return [-1, -1]
		else:
			radiuses.append(radius)
	else:
		return [a, b] if a > 0 and a >= b else [-1, -1]


def main():
	print answer(map(int, raw_input().split()))


main()
