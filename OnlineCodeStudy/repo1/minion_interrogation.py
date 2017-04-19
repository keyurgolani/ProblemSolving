from __future__ import division
def answer(minions):
    ''' Return the fastest expected minion interrogation order given a list
        of [time, prob_numerator, prob_denominator] minion info.
    '''
    num_minons = len(minions)
    assert 2 <= len(minions) <= 50

    # dividing the time by the probability of success gives the
    # individual expected interrogation time, so trying them
    # in order of this criterion will give the best overall time
    sortkey = [t/(n/d) for t, n, d in minions]

    # timsort is stable, so we don't have to worry about having the
    # lexicographically first solution if we sort an ordered list
    return sorted(range(num_minons), key = sortkey.__getitem__)



import itertools
def check_permutations(minions):
    perms = [(evaluate_expected_time(x,minions),x)
                for x in itertools.permutations(range(len(minions)))]
    perms.sort()
    return perms[0]

def evaluate_expected_time(order, minions):
    prob_of_nth_interrogation = 1
    expected_time = 0
    for i in order:
        interrogation_time = minions[i][0]
        expected_time += prob_of_nth_interrogation * interrogation_time
        prob_of_nth_interrogation *= 1 - minions[i][1]/minions[i][2]
    return expected_time

minions1 = [[5, 1, 5], [10, 1, 2]]
result1 = answer(minions1)
print result1
print result1 == [1, 0]
print evaluate_expected_time(result1, minions1)
minions2 = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
result2 = answer(minions2)
print result2
print result2 == [2, 3, 0, 1]
print evaluate_expected_time(result2, minions2)
