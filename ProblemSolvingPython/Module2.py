import sys
import Utilities as Util


def greedy_sort(values):
    sorted_values = []
    for idx in range(len(values)):
        current_max = max(values)
        sorted_values.append(current_max)
        values.remove(current_max)
    return sorted_values