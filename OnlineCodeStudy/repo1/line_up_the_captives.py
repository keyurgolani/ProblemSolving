# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:30:07 2015

@author: richard
"""
import math

def answer(x, y, n):
    ''' return the number of ways to position n items in a line such that
    x are visible from the left and y are visible from the right.

    each item has a height, and taller ones block shorter ones from sight

    need to return the answer as a string for no reason
    '''
    assert 3<=n<=40
    assert 1<=x<=n
    assert 1<=y<=n

    orders = [([n],x-1,y-1)]
    blockers = []
    for h in reversed(range(1,n)):
        neworders = []
        if not orders:
            h+=1
            break
        while orders:
            order,left_needed, right_needed = orders.pop()
            if right_needed:
                neworders.append((order+[h],left_needed,right_needed-1))
            if left_needed:
                neworders.append(([h]+order,left_needed-1,right_needed))
            if not (right_needed or left_needed):
                blockers.append(order)
        orders = neworders
    else:
        h=0
        for order, left_needed, right_needed in orders:
            if not (right_needed or left_needed):
                blockers.append(order)

    p = len(blockers)
    print('blocker permutations',p)
    l = len(blockers[0])
    print('number of blockers needed',l)
    ways = 0
    for blocker_order in blockers:
        l = len(blocker_order)
        for i in range(l):
            ways += stirling_number(h,i)*math.factorial(h)#*(l-i)
    return str(ways)

def stirling_number(n,k,memo={}):
    if (n,k) in memo:
        return memo[(n,k)]
    if not (n or k):
        return 1
    if not n or not k:
        return 0

    ans = memo[(n,k)] = k*stirling_number(n-1,k)+stirling_number(n-1,k-1)
    return ans

def add_blocker(blockers,blocker,left_needed,right_needed):
    if not blocker:
        return 0
    ans = 0
    if left_needed>0:
        ans = 1 + add_blocker([blocker]+blockers,blocker-1,left_needed-1,right_needed)
    if right_needed>0:
        ans = 1 + add_blocker(blockers+[blocker],blocker-1,left_needed,right_needed-1)
    return ans



def slowanswer(x, y, n):
    ''' return the number of ways to position n items in a line such that
    x are visible from the left and y are visible from the right.

    each item has a height, and taller ones block shorter ones from sight

    need to return the answer as a string for no reason
    '''
    assert 3<=n<=40
    assert 1<=y<=n
    assert 1<=x<=n

    heights = list(range(1,n+1))

    solutions = 0

    for perm in itertools.permutations(heights):
            if validate(perm,x,y):
                print(perm)
                solutions+=1

    return str(solutions)

def validate(heights,x,y):
    maxheight=0
    leftvisible=0
    for height in heights:
        if height > maxheight:
            leftvisible +=1
            maxheight = height
    if leftvisible != x:
        return False
    maxheight = 0
    rightvisible = 0
    for height in reversed(heights):
        if height > maxheight:
            rightvisible +=1
            maxheight = height
    return rightvisible == y

import itertools

x=2
y=2
n=3

a = answer(x,y,n)
b = slowanswer(x,y,n)
print(a, '=', b)

x=1
y=2
n=6

a = answer(x,y,n)
b = slowanswer(x,y,n)
print(a, '=', b)

x=2
y=4
n=9
a = answer(x,y,n)
b = slowanswer(x,y,n)
print(a, '=', b)

def permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for p in permutations(s[:i] + s[i+1:]):
                yield [s[i]] + p