def next_hop(towers, current):
    max_reach_potential = current
    potential_next_hop = current
    for step in range(towers[current]):
        if current + step + 1 >= len(towers):
            return current + step + 1
        if current + step + 1 + towers[current + step + 1] > max_reach_potential:
            max_reach_potential = current + step + 1 + towers[current + step + 1]
            potential_next_hop = current + step + 1
    return potential_next_hop


def answer(towers):
    current = 0
    while True:
        if current >= len(towers):
            return True
        if towers[current] == 0:
            return False
        current = next_hop(towers, current)


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case + 1, answer(map(int, raw_input().split())))


if __name__ == '__main__':
    main()
