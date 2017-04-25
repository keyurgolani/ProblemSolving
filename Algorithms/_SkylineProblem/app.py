import heapq


def skyline(buildings):
    start_points = sorted(map(lambda x: (x[0], x[2]), buildings))
    end_points = sorted(map(lambda x: (x[1], x[2]), buildings))
    # TODO: Implement the method using heapq
    return buildings


def main():
    for case in range(int(raw_input())):
        buildings = []
        for _ in range(int(raw_input())):
            buildings.append(tuple(raw_input().split()))
        print "Case #{}".format(case)
        for coordinate in skyline(buildings):
            print "X: {}\tY: {}".format(coordinate[0], coordinate[1])


if __name__ == '__main__':
    main()
