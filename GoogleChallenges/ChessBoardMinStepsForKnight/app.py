def answer(src, dest):
	src_y, src_x = divmod(src, 8)
	dest_y, dest_x = divmod(dest, 8)
	x_diff = abs(src_x - dest_x)
	y_diff = abs(src_y - dest_y)
	if x_diff == y_diff == 1 or x_diff == y_diff == 2:
		return 4
	elif x_diff + y_diff == 1:
		return 3
	elif (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2):
		return 1
	elif x_diff == y_diff == 7:
		return 6
	else:
		max_m = int(round(max(x_diff/2.0, y_diff/2.0, (x_diff + y_diff)/3)))
		return max_m + ((max_m + x_diff + y_diff) % 2)


def main():
	print answer(*tuple(map(int, raw_input().split())))


main()
