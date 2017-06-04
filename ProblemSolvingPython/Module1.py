import sys


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


def max_pairwise_product(values):
    """
    Function that accepts an array of integer values and returns maximum pairwise product from the array
    :param values: an array of integer values
    :return: maximum pairwise product from the input values
    """
    if len(values) <= 1:
        return None
    max_one = -sys.maxint - 1
    max_two = -sys.maxint - 1
    min_one = sys.maxint
    min_two = sys.maxint
    for value in values:
        if value >= max_one:
            max_two = max_one
            max_one = value
        if max_one > value >= max_two:
            max_two = value
        if value <= min_one:
            min_two = min_one
            min_one = value
        if min_one < value <= min_two:
            min_two = value

    print max_one, max_two, min_one, min_two
    min_product = min_one * min_two
    max_product = max_one * max_two
    return min_product if min_product > max_product else max_product


def max_pairwise_sum(values):
    """
    Function that accepts an array of integer values and returns maximum pairwise sum from the array
    :param values: an array of integer values
    :return: maximum pairwise sum from the input values
    """
    if len(values) <= 1:
        return None
    max_one = -sys.maxint - 1
    max_two = -sys.maxint - 1
    for value in values:
        if value >= max_one:
            max_two = max_one
            max_one = value
    return max_one + max_two


def fibonacci_series(limit):
    """
    Yields the value of fibonacci series at current index below the limit
    :param limit: limit integer to generate fibonacci series upto
    :return: yields fibonacci value of current idx
    """
    fibonacci = [0, 1]
    for idx in range(limit):
        if idx <= 1:
            yield fibonacci[idx]
        else:
            fibonacci.append(fibonacci[idx - 1] + fibonacci[idx - 2])
            yield fibonacci[idx]


def fibonacci_number(position):
    """
    Returns the value of number at given position in fibonacci series
    :param position: position to return number at from fibonacci series
    :return: returns the integer number at position from fibonacci series
    """
    fibonacci = [0, 1]
    for idx in range(position):
        if idx > 1:
            fibonacci.append(fibonacci[idx - 1] + fibonacci[idx - 2])
    return fibonacci[position - 1]


def fibonacci_number_last_digit(position):
    """
    Returns the last digit of number at given position in fibonacci series
    :param position: position to return number at from fibonacci series
    :return: returns the integer last digit of number at position from fibonacci series
    """
    fibonacci = [0, 1]
    for idx in range(position):
        if idx > 1:
            fibonacci.append((fibonacci[idx - 1] + fibonacci[idx - 2]) % 10)
    return fibonacci[position - 1]


def gcd(number_one, number_two):
    """
    Gives Greatest Common Divisor for the numbers passed
    Used Euclidean Algorithm
    :param number_one: Integer Number one for GCD
    :param number_two: Integer Number two for GCD
    :return: Integer Greatest Common Divisor for two numbers input
    """
    print number_one, number_two
    while number_two != 0:
        number_one, number_two = number_two, number_one % number_two
    return number_one
