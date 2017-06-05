import sys
import Utilities as Util


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
    for idx in range(limit+1):
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
    for idx in range(position+1):
        if idx > 1:
            fibonacci.append(fibonacci[idx - 1] + fibonacci[idx - 2])
    return fibonacci[position]


def fibonacci_number_last_digit(position):
    """
    Returns the last digit of number at given position in fibonacci series
    :param position: position to return number at from fibonacci series
    :return: returns the integer last digit of number at position from fibonacci series
    """
    fibonacci = [0, 1]
    for idx in range(position+1):
        if idx > 1:
            fibonacci.append((fibonacci[idx - 1] + fibonacci[idx - 2]) % 10)
    return fibonacci[position]


def fibonacci_number_modulo(position, number):
    """
    Returns the fibonacci number at given position modulo given number
    :param position: position for the fibonacci number in fibonacci series
    :param number: number to modulo fibonacci number with
    :return: integer modulo value of fibonacci number at position with given number
    """
    if number == 0:
        return fibonacci_number(position)
    elif number == 1:
        return 0
    else:
        pattern_position = position % Util.get_pisano_period(number)
        return fibonacci_number(pattern_position) % number


def last_digit_of_sum_of_fibonacci_numbers_till(limit):
    """
    Returns last digit of sum of fibonacci numbers till limit
    :param limit: limit till which to sum the fibonacci numbers
    :return: returns integer last digit of sum of all fibonacci numbers till given limit
    """
    sum = 0
    fibonacci = [0, 1]
    for idx in range(limit + 1):
        if idx <= 1:
            sum += fibonacci[idx] % 10
        else:
            fibonacci[0], fibonacci[1] = fibonacci[1], fibonacci[0] + fibonacci[1]
            sum += fibonacci[1] % 10
    return sum % 10


def last_digit_of_partial_sum_of_fibonacci_numbers(start, end):
    """
    Returns last digit of partial sum of fibonacci numbers from start till end
    :param start: start position of the partial sum in series
    :param end: end position of the partial sum in series
    :return: returns integer last digit of partial sum of all fibonacci numbers from start till end
    """
    sum = 0
    fibonacci = [0, 1]
    for idx in range(start):
        if idx > 1:
            fibonacci[0], fibonacci[1] = fibonacci[1], fibonacci[0] + fibonacci[1]
    for idx in range(start, end+1):
        if idx <= 1:
            sum += fibonacci[idx] % 10
        else:
            fibonacci[0], fibonacci[1] = fibonacci[1], fibonacci[0] + fibonacci[1]
            sum += fibonacci[1] % 10
    return sum % 10



def gcd(number_one, number_two):
    """
    Gives Greatest Common Divisor for the numbers passed
    Used Euclidean Algorithm
    :param number_one: Integer Number one for GCD
    :param number_two: Integer Number two for GCD
    :return: Integer Greatest Common Divisor for two numbers input
    """
    while number_two != 0:
        number_one, number_two = number_two, number_one % number_two
    return number_one


def lcm(number_one, number_two):
    """
    Gives Greatest Common Divisor for the numbers passed
    Used Euclidean Algorithm
    :param number_one: Integer Number one for GCD
    :param number_two: Integer Number two for GCD
    :return: Integer Greatest Common Divisor for two numbers input
    """
    return number_one * number_two / gcd(number_one, number_two)
