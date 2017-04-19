# -*- coding: utf-8 -*-

from __future__ import division

import math
import itertools
CHOICES = '-RL'


def answer(x):
    ''' Given a object with mass x, output a list of balancing
        instruction characters.

        The cube of the index plus one indicates the mass to use.
        "L", "R", and "-" indicate whether to use it on the left, right,
        or not at all.

        Remember, the object starts on the left, so we need a combo that
        has a net weight of x on the right.

        Based on balanced ternary carrying example from math stackexchange
    '''
    assert x <= 1000000000

    weights = {}
    while x:
        index = math.floor(math.log(x,3))
        x = x - 3**index
        add_weight(weights,index)

    instruction_list = []
    index=0
    while weights:
        if index in weights:
            instruction_list.append(CHOICES[weights[index]])
            del weights[index]
        else:
            instruction_list.append('-')
        index = index + 1

    return instruction_list


def add_weight(weights, index):
    usage = weights[index] = weights.get(index,0) + 1
    assert usage in {-1,0,1,2}
    if usage == 2:
        weights[index] = -1
        add_weight(weights,index+1)


def answer2(x):
    weights = []
    while x:
        index = math.floor(math.log(x,3))
        x = x - 3**index
        add_weight2(weights,index)

    return [CHOICES[weight] for weight in weights]

def add_weight2(weights,index):
    while index >= len(weights):
        weights.append(0)
    usage = weights[index] = weights[index] + 1
    if usage == 2:
        weights[index] = -1
        add_weight2(weights, index+1)

def oldanswer(x):
    ''' Given a object with mass x, output a list of balancing
        instruction characters.

        The cube of the index plus one indicates the mass to use.
        "L", "R", and "-" indicate whether to use it on the left, right,
        or not at all.

        Remember the object starts on the left.

        I even though I felt like there should be an algebraic answer,
        I tried BFS. Too slow though, apparently.
    '''
    assert x <= 1000000000

    l = 0
    while True:
        l += 1
        for instructions in instruction_generator(l):
            if test_instructions(instructions, x):
                while instructions[-1] == '-':
                    instructions.pop()
                return instructions


def instruction_generator(l):
    assert l>0
    if l == 1:
        for perm in itertools.permutations(CHOICES):
            for instruction in perm:
                yield [instruction]
    else:
        for instructions in instruction_generator(l-1):
            for instruction in instruction_generator(1):
                instructions.extend(instruction)
                yield instructions
                instructions.pop()


def test_instructions(instructions, x):
    left, right = x, 0
    for mass_index, instruction in enumerate(instructions):
        if instruction == 'L':
            left+=(3**(mass_index))
        elif instruction == 'R':
            right+=(3**(mass_index))
        elif instruction == '-':
            continue
        else:
            raise ValueError('Undefined instruction')
    return (left) == (right)




if __name__ == '__main__':
    print(0,['-'])
    for i in range(1,100):
        a = answer2(i)
        print(i,a)
        print(test_instructions(a,i))