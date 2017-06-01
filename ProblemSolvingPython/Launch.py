import sys

import Module1 as m1

input_values = sys.stdin.readline()
values = map(int, input_values.split(" "))
print m1.sum_of_numbers(values)
