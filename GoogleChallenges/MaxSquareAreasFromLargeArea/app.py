import math

def answer(area):
    remainingArea = area
    areaList = []
    while remainingArea != 0:
        currentArea = int(math.sqrt(remainingArea))**2
        remainingArea -= currentArea
        areaList.append(currentArea)
    return areaList


def main():
    print answer(2353454)
    print answer(2453)
    print answer(234)
    print answer(100000000)
    print answer(34345)
    print answer(23233)
    print answer(2234)


main()
