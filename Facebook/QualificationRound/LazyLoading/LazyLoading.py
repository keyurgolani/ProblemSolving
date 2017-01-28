import sys
import math

def Solve(weights):
    trip_counts = 0
    while True:
        current_total_weight = 0
        try:
            popped_value = weights.pop(weights.index(max(weights)))
        except ValueError:
            break
        except IndexError:
            break
        else:
            current_total_weight += popped_value
            additional_item_count = math.ceil(50.0 / popped_value) - 1
            for item in range(int(additional_item_count)):
                try:
                    weights.pop(weights.index(min(weights)))
                except ValueError:
                    break
                except IndexError:
                    break
                else:
                    current_total_weight += popped_value
        if current_total_weight < 50:
            pass
        else:
            trip_counts += 1
    return trip_counts


T = int(sys.stdin.readline())
f = open('lazy_loading_output.txt', 'w')
for t in range(T):
    N = int(sys.stdin.readline())
    w = []
    for n in range(N):
        w.append(int(sys.stdin.readline()))
    f.write("Case #{}: {}\n".format(t + 1, Solve(w)))
f.close()
