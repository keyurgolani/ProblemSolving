import sys
import math

def Solve(P, x, y):
    if ((50.0-x)**2.0 + (50.0-y)**2.0)**(1.0/2.0) > 50.0:
        return "white"
    else:
        point_angle = math.atan(((50.0-y)/(50.0-x)))
        if point_angle > P * 2.0 * math.pi / 100:
            return "white"
        else:
            return "black"

T = int(sys.stdin.readline())
for t in range(T):
    P, x, y = map(int, sys.stdin.readline().split())
    print "Case #{}: {}".format(t + 1, Solve(P, x, y))
