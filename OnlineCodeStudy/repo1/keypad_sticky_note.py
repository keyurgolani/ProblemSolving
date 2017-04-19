def answer(s, x):
    ''' Finds the number of pairs (a, b) that have the target sum and xor.

        Use brute force only after checking the few special cases I could see
    '''

    # The lowest bit of x and s must match, because they mismatch due to
    # carry-in''
    if not s % 2 == x % 2:
        return 0
    # x == 0 implies a == b, so (a,b) and (b,a) are identical
    if x == 0:
        return 1
    # x == s is always valid, so return the pairs without looping
    if x == s:
        return pairs(x)

    # After much head/wall induced inspiration, I couldn't think of any other
    # shortcuts, so just brute force it

    # cut worst-case complexity by half by noticing that any a over s/2 represents
    # a swap of a pair we have already counted
    for a in xrange(s / 2 + 1):
        if s - a == x ^ a:
            return pairs(x)

    return 0


def pairs(x):
    ''' Return the number of pairs implied by x, when x is a valid pair with s
        and x>0.

        By inspection of the brute-force count, whenever x is a valid choice
        the count of pairs is 2**(number of 1 bits i.e. popcount)

        Perhaps this is because each x bit contributes an ambiguous pair
        and we have to select permutations
    '''

    # This is a relatively fast way to do binary popcount in python
    popcount = sum(int(b) for b in bin(x)[2:])
    return 2**popcount

import math


def bad_valid_x(s, memo={}):
    ''' sort of a weird symmetry around every 2**n-1
    the set of valid x for 2**n-1+d is the same as that for 2**n-1-d, plus some extras

    the new ones appear to be
    the same as the set of valid x for d, but plus 2**n

    but it doesn't seem to work
    '''
    if s in memo:
        return memo[s]
    a = math.log(s + 1, 2)
    n = int(math.floor(a))

    if n == a:
        memo[s] = {s}
        return memo[s]

    two_pow_n = 2**n

    # s+1 == 2**n + d
    d = s - two_pow_n + 1

    lower_x = bad_valid_x(two_pow_n - d - 1)
    higher_x = set(x + two_pow_n - 1 for x in bad_valid_x(d))
    print lower_x
    print higher_x
    memo[s] = lower_x | higher_x
    return memo[s]


def slowanswer(s, x):
    ''' Finds the number of pairs (a, b) that have the target sum and xor.

        given s = a + b, b = s - a
        given x = a ^ b, a = x ^ b

        therefore the system is determined modulo something

        xor is addition without carrying!!
        x = a ^ b = mod(a+b, 2) for each bit

        evidently the number of ones in bits(x) is the answer
        IF s and x are a valid combination

        perhaps this is because each x bit contributes an ambiguous pair
        and we have to select permutations

        we need to determine if an input pair is valid...

        There seems to be a pattern in the possibilities for x that propagates
        symmetrically around each s = 2**n - 1

        maybe we can interrogate something about the bits using &

    '''
    assert 0 <= s <= int(2e9)
    assert 0 <= x <= int(2e9)

    if not s % 2 == x % 2:
        return 0
    if x == s:
        return 2**sum(int(b) for b in bin(x)[2:])
    if x == 0:
        return 1

    pairs = 0
    for a in xrange(s / 2 + 1):
        pairs += s - a == x ^ a
#        b = s-a
#        if x == a^b:
#            if a == b: # this only happens at x=0
#                pairs +=1
#            else:
#                pairs +=2
    return 2 * pairs


def hint(a, b):
    #    print (bin(a),bin(b))
    return (a + b, a ^ b)

print answer(10, 4) == 2
print answer(0, 0) == 1
print answer(5, 3) == 0


def helper(s):
    print 's: {:>3d}'.format(s), '{:>10b}'.format(s)
    print '-------------------'
    for x in range(s + 1):
        a = slowanswer(s, x)
        print 'x: {:>3d}'.format(x), '{:>10b}'.format(x), a if a else 'x', '{:>10b}'.format(s ^ x)

#import timeit

# print min(timeit.repeat(lambda:answer(*hint(int(1e6),int(7e6))), number=1))

# for n in range(17):
#    helper(n)
#    print '\n'
