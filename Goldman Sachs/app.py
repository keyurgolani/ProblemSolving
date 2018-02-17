def fib(n):
    if n <= 1:
        return n
    elif n == 2:
        return fib(n-1) + fib(n-2)
    return fib(n-1) + fib(n-2) + fib(n-3)

def countWays(s):
    if s == 0:
        return 0
    return fib(s + 1)

s = 4
print "Number of ways = ",
print countWays(s)