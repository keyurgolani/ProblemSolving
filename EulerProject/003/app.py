import sys
import math


def factorize(n):
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n + 1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n + i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res


# Naive Solution Helper
def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print '\t', f
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

# Naive Solution


def answer(num):
    if num % 2 == 0:
        while num % 2 == 0:
            num /= 2
        potential_factor = num - 1
        while potential_factor > 2:
            if num % potential_factor == 0 and isPrime(potential_factor):
                return potential_factor
            potential_factor -= 2
        else:
            return 2
    else:
        potential_factor = num - 2
        while potential_factor > 2:
            if num % potential_factor == 0 and isPrime(potential_factor):
                return potential_factor
            potential_factor -= 2
        else:
            return 1


def answer2(num):
    return max(factorize(num))


def main():
    idx = 0
    for line in sys.stdin:
        print "Case #{}: {}".format(idx, answer2(int(line)))
        idx += 1


if __name__ == '__main__':
    main()
