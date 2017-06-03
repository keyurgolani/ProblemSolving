import sys
import time


# Taking inputs
def take_int_array_input():
    """
    Takes an array from the stdin as input and returns it formatting in an array of integers.
    :return: Array of integers taken from stdin
    """
    return map(int, sys.stdin.readline().split(" "))


def take_int_input(how_many):
    """
    Takes 'how_many' integer inputs from stdin and returns them as a tuple
    :param how_many: integer count denoting how many inputs to take from stdin
    :return: tuple with 'how_many' integers taken from stdin
    """
    return tuple(map(int, sys.stdin.readline().split(" "))[:how_many])


def timeit(closure):
    start = time.time()
    closure()
    print "\n\n----------------------------------------"
    print "Execution Time: {time} seconds".format(time=(time.time() - start) / 1000)
    print "----------------------------------------\n\n"
