def answer(m):
    states_count = len(m)
    state_outcomes = [0]*states_count
    navigation_matrix = m[:]
    terminal_states = [all(map(lambda x: not x > 0, state)) for state in m]
    iterations = reduce(lambda x, y: x * y, filter(lambda x: x > 0, map(lambda x: reduce(lambda a, b: a + b, x), m)))
    for iteration in xrange(iterations):
        print '-'*20
        current_state = 0
        states_visited = [False] * states_count
        while not terminal_states[current_state]:
            for idx, element in enumerate(navigation_matrix[current_state]):
                print m
                if element > 0:
                    navigation_matrix[current_state][idx] -= 1
                    next_state = idx
                    break
            else:
                navigation_matrix[current_state] = m[current_state]
            current_state = next_state
        else:
            state_outcomes[current_state] += 1
    return state_outcomes


def main():
    print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))


main()
