import random

class Node(object):

    def __init__(self, next_node_map):
        self.probabilities = next_node_map
        self.set_denominator()

    def set_denominator(self):
        self.denominator = 0 if any(map(lambda x: x < 0, self.probabilities)) else sum(self.probabilities)


    def is_terminal(self):
        return self.denominator == 0


    def random_next_state(self):
        num = random.randint(0, self.denominator)
        for idx, probability in enumerate(self.probabilities):
            if num < probability:
                return idx
            if probability < 1:
                continue
            num -= probability
        return -1


class FractionProcessor(object):
    @staticmethod
    def GCM(x, y):
        return x if y == 0 else gcm(y, x % y)

    @staticmethod
    def LCM(x, y):
        return (x * y) / GCM(x, y)

    @staticmethod
    def GetFraction(value):
        tolerance = 0.001
        p1 = 1
        q1 = 0
        p2 = 0
        q2 = 1

        b = value
        while True:
            a = int(b)
            aux = p1
            p1 = a * p1 + p2
            p2 = aux
            aux = q1
            q1 = a * q1 + q2
            q2 = aux
            b = 1 / (b - a)
            if abs(value - p1 / q1) <= value * tolerance:
                break


def answer(m):
    state_nodes = map(lambda x: Node(x), m)
    is_terminal = map(lambda x: x.is_terminal(), state_nodes)
    terminal_states_count = sum(is_terminal)

    state_counts = [0] * len(state_nodes)

    current_state = 0
    depth_limit = 10
    success = True
    # simulations_count = 17777777
    simulations_count = 18
    successful_simulations = 0
    for _ in xrange(simulations_count):
        current_state = 0
        depth_limit = 10
        success = True
        while not is_terminal[current_state]:
            if depth_limit <= 0:
                success = False
                break
            depth_limit -= 1
            current_state = state_nodes[current_state].random_next_state()
        if success:
            state_counts[current_state] += 1
            successful_simulations += 1

    print state_counts
    print successful_simulations


def main():
    print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))


main()
