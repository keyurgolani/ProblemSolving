import re
import numpy as np
import math

# TODO: Not optimized. Needs optimization.
isPrime = lambda number: not any(map(lambda x: float(number)/x == number/x, primesfrom2to(number)))

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


def ReIDWithPrimes(draw_number):
    prime_list = []
    page = 100
    current_number = 0
    str_length = 0
    while str_length < draw_number + 5:
        if current_number != 0 and current_number != 1:
            if isPrime(current_number):
                prime_list.append(current_number)
                str_length += len(str(current_number))
        current_number += 1
    return ''.join(map(str, prime_list))[draw_number:]


def main():
    print ReIDWithPrimes(10000)


main()
