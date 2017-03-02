import sys

def answer(floors, rooms, X, Y):
    total_count = 0
    for floor in range(1, floors + 1):
        initial_room = int(str(floor) + '01')
        total_count += int((initial_room + rooms[floor - 1] - 1 )/ X)
        total_count += int((initial_room + rooms[floor - 1] - 1) / Y)
        total_count -= int((initial_room + rooms[floor - 1] - 1) / (X * Y))
        total_count -= int((initial_room - 1) / X)
        total_count -= int((initial_room - 1) / Y)
        total_count += int((initial_room - 1) / (X * Y))
    return total_count

def main():
    for _ in range(1, int(raw_input())+1):
        discard = raw_input()
        floors = int(raw_input())
        rooms = map(int, raw_input().split())
        X, Y = map(int, raw_input().split())
        print 'Case #{}: {}'.format(_, answer(floors, rooms, X, Y))


main()


# 2
# 1
# 1
# 101 102
# 1
# 4
# 2 7
