from sys import stdin


def sum_of_numbers(values):
    """
    Function that accepts an array of integer values and returns the sum of all the integer values
    :param values: an array of integer values to be summed
    :return: sum of all integer values passed as input parameter
    """
    answer = 0
    for value in values:
        answer += value
    return answer
