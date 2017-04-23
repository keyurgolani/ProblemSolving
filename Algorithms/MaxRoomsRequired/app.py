def answer(timings):
    max_rooms = 0
    checkins = sorted(map(lambda x: x[0], timings))
    checkouts = sorted(map(lambda x: x[1], timings))
    idx = 0
    idy = 0
    rooms = 0
    while idx < len(checkins) or idy < len(checkouts):
        if idx == len(checkouts) or checkins[idx] >= checkouts[idy]:
            rooms -= 1
            idy += 1
        else:
            rooms += 1
            idx += 1
        if rooms > max_rooms:
            max_rooms = rooms
    return max_rooms


def main():
    for case in range(int(raw_input())):
        timings = []
        for _ in range(int(raw_input())):
            checkin, checkout = map(int, raw_input().split())
            timings.append((checkin, checkout))
        print "Case #{}: {}".format(case, answer(timings))


if __name__ == '__main__':
    main()
