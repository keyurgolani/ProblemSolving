def minConsecutiveSubArrayToSort(unsorted_list):
    sorted_list  = sorted(unsorted_list)
    count = 0
    for idx, element in enumerate(unsorted_list):
        if element == sorted_list[idx]:
            count += 1
        else:
            break
    for idx, element in enumerate(unsorted_list[::-1]):
        if element == sorted_list[-idx-1]:
            count += 1
        else:
            break
    return 0 if count == 2 * len(unsorted_list) else len(unsorted_list) - count


def main():
    while True:
        print minConsecutiveSubArrayToSort(map(int, raw_input('Input: ').split()))


main()
