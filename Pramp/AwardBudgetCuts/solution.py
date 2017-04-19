def answer(grants, new_budget):
    # Will do a while loop till the budget cut is 0
    # Will keep decresing the budget cut as we keep adjusting cap
    # Initially cap will be the max grant out of all and
    # budget cut will be the difference in total previous budget and new budget.
    # When budget_cut is compensated into cap, budget cut will become 0 and we will return cap.
    budget_cut = sum(grants) - new_budget
    cap = max(grants)
    while budget_cut > 0:
        current_max = max(grants)
        current_max_count = grants.count(current_max)
        without_max = filter(lambda x: x != current_max, grants)
        current_second_max = max(without_max) if len(without_max) > 0 else 0
        # If capping the current max grant to current second max grant keeps total budget more than new budget
        # Decrease the cap to current second max and decrease the budget cut by the difference multiplied by number of max grants
        if (current_max - current_second_max) * current_max_count <= budget_cut:
            cap -= current_max - current_second_max
            budget_cut -= (current_max - current_second_max) * current_max_count
            # Make all max grants equal to second max grant after adjusting the cap
            grants = map(lambda x: x if x < current_max else current_second_max, grants)
        else:
            # If capping the current max grant to current second max grant makes total budget less than new budget
            cap -= budget_cut / current_max_count
            budget_cut = 0
    return cap


def main():
    # Iterating through each case
    for case in xrange(int(raw_input())):
        # Taking grants
        grants = map(int, raw_input().split())
        # Taking new budget.
        new_budget = int(raw_input())
        # Printing output from "answer" function in right format
        print 'Case #{}: {}'.format(case+1, answer(grants, new_budget))


if __name__ == '__main__':
    main()
