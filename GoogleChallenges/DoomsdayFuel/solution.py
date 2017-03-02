from fractions import Fraction as F

def terminal_submatrices(mat, terminal_states):
    n2t = []
    n2n = []
    for row, is_src_terminal in zip(mat, terminal_states):
        n2t_row = []
        n2n_row = []
        for element, is_dst_terminal in zip(row, terminal_states):
            if not is_src_terminal:
                if is_dst_terminal:
                    n2t_row.append(element)
                else:
                    n2n_row.append(element)
        if n2t_row:
            n2t.append(n2t_row)
        if n2n_row:
            n2n.append(n2n_row)
    return n2t, n2n


def reduce_to_probabilities(R, Q):
    denominators = map(lambda x, y: reduce(lambda a, b: a + b, x + y), R, Q)
    return map(lambda x, y: map(lambda a: a / y, x), R, denominators), map(lambda x, y: map(lambda a: a / y, x), Q, denominators)


def get_identity(size):
    return [[F(1, 1) if y == x else F(0, 1) for y in range(size)] for x in range(size)]


def subtract_matrices(M1, M2):
    return map(lambda x, y: map(lambda a, b: a - b, x, y), M1, M2)


def transpose(M1):
    if len(M1) > 0:
        return [[row[i] for row in M1] for i in range(len(M1[0]))]
    else:
        return M1


def getMatrixMinor(M1, i, j):
    return [row[:j] + row[j+1:] for row in (M1[:i] + M1[i+1:])]


def getMatrixDeternminant(M1):
    #base case for 2x2 matrix
    if len(M1) == 2:
        return M1[0][0] * M1[1][1] - M1[0][1] * M1[1][0]
    determinant = 0
    for c in range(len(M1)):
        determinant += ((-1) ** c) * M1[0][c] * getMatrixDeternminant(getMatrixMinor(M1, 0, c))
    return determinant


def inverse(M1):
    determinant = getMatrixDeternminant(M1)
    #special case for 2x2 matrix:
    if len(M1) == 2:
        return [[M1[1][1] / determinant, -1 * M1[0][1] / determinant],
                [-1 * M1[1][0] / determinant, M1[0][0] / determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(M1)):
        cofactorRow = []
        for c in range(len(M1)):
            minor = getMatrixMinor(M1, r, c)
            cofactorRow.append(((-1)**(r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def multiply(M1, M2):
    return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*M2)] for X_row in M1]

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y / gcd(x, y)


def answer(m):
    terminal_states = [all(map(lambda x: not x > 0, state)) for state in m]
    fraction_m = map(lambda row: map(lambda x: F(x, 1), row), m)
    R, Q = terminal_submatrices(fraction_m, terminal_states)
    R, Q = reduce_to_probabilities(R, Q)
    G = inverse(subtract_matrices(get_identity(len(Q)), Q))
    GR = multiply(G, R)
    if len(GR) > 0:
        denominator = reduce(lambda x, y: lcm(x, y), map(lambda x: x.denominator, GR[0]))
        return map(lambda x: x.numerator * denominator / x.denominator, GR[0]) + [denominator]
    else:
        answer = [0]*len(m)
        answer[0] = 1
        return answer + [1]


def main():
    # print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
    # print(answer([]))
    print(answer([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    # print(answer([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]))
    # print(answer([[0]]))
    # print(answer([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
    # print(answer([[0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
    # print(answer([[0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))


main()
