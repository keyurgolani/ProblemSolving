def f1(a, L=""):
    L += str(a)
    return L

print(f1(1))
print(f1(2))
print(f1(3))


def f2(a, L=[]):
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))


def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f3(1))
print(f3(2))
print(f3(3))
