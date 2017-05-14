# Partition a list into a list of tuples of N elements
# Converting [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] into [(1, 2), (3, 4), (5, 6),
# (7, 8), (9, 10)] or [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 3
o = zip(*[iter(l)] * N)
print o


# Take a string input containing integers and convert to integer list

s = '5 2 8 4 3 3 5 6 2 4'
# Replace s.split() with raw_input().split() while dealing with stdin
o = map(int, s.split())
print o


# Flattening a list of lists
ll = [[1, 2], [3, 4], [5, 6]]
o = reduce(lambda l1, l2: l1 + l2, ll)
import itertools
o = list(itertools.chain.from_iterable(ll))
print o


# Flattening a list of tuples
lt = [(1, 2), (3, 4), (5, 6)]
o = reduce(lambda l1, l2: list(l1) + list(l2), lt)
import itertools
o = list(itertools.chain.from_iterable(lt))
print o

# Getting a list of N zeros
N = 10
# Don't do this with objects or dictionaries. It makes one object and
# lists N different references to the same object. Unless you're trying to
# do it!
nz = [0] * N
print nz
