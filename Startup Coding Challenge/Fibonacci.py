import sys
sys.setrecursionlimit(10000)
stored_calculations = {}
def answer(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        numMinusOne = 0
        numMinusTwo = 0
        if (num - 1) in stored_calculations.keys():
            numMinusOne = stored_calculations[num - 1]
        else:
            numMinusOne = answer(num - 1)
            stored_calculations[(num - 1)] = numMinusOne
        if (num - 2) in stored_calculations.keys():
            numMinusTwo = stored_calculations[num - 2]
        else:
            numMinusTwo = answer(num - 2)
            stored_calculations[(num - 2)] = numMinusTwo
        return numMinusOne + numMinusTwo

print(answer(8181))
