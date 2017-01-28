import sys
import itertools

# Time Complexity too much. Program exiting before processing the input. Needs optimization.
def Solve(d, rolls):
    max_probability = 0
    max_damage = 0
    best_die_roll = None
    best_add = 0
    best_sub = 0
    for roll in rolls:
        add = 0
        sub = 0
        die_roll = None
        if "+" in roll:
            die_roll = roll.split("+")[0]
            add = int(roll.split("+")[1])
        elif "-" in roll:
            die_roll = roll.split("-")[0]
            sub = int(roll.split("-")[1])
        else:
            die_roll = roll
        damage = int(die_roll.split("d", 2)[0]) * int(die_roll.split("d", 2)[1]) + add - sub
        if damage > max_damage:
            max_damage = damage
            best_add = add
            best_sub = sub
            best_die_roll = die_roll
    zombie_kill = 0
    zombie_live = 0
    for combination in list(itertools.product([x+1 for x in range(int(best_die_roll.split("d", 2)[1]))], repeat = int(best_die_roll.split("d", 2)[0]))):
        total = float(sum(i for i in combination)) + best_add - best_sub
        if total >= d:
            zombie_kill += 1
        else:
            zombie_live += 1
    return float(zombie_kill) / float(zombie_kill + zombie_live)


T = int(sys.stdin.readline())
f = open('fighting_zombie_output.txt', 'w')
for t in range(T):
    d, N = map(int, sys.stdin.readline().split())
    rolls = sys.stdin.readline().split()
    # print("Case #{}: {}\n".format(t + 1, Solve(d, rolls)))
    f.write("Case #{}: {}\n".format(t + 1, Solve(d, rolls)))
f.close()
