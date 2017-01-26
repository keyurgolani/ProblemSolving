def replacePartOfBinaryString(s1, s2, i, j):
	return s1[:min(i, j)] + s2 + s1[max(i, j)+1:]


def main():
	print replacePartOfBinaryString('10000000000', '10101', 2, 6)
	print replacePartOfBinaryString('10010100010110', '1010011', 4, 1)
	print replacePartOfBinaryString('1001000100100', '10110101', 3, 4)
	print replacePartOfBinaryString('1001010101110', '0010110', 8, 1)
	print replacePartOfBinaryString('100110010100', '1101010', 5, 2)
	print replacePartOfBinaryString('11101101010101100', '00000000', 5, 5)

# 10 10101 0000
# 1 1010011 100010110
# 1001011010100100100
# 100101101110
# 101101010010100
# 111010000000001010101100


main()
