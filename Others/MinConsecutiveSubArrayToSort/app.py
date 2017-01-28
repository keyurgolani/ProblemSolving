def minConsecutiveSubArrayToSort(unsorted_list):
    # start_index = -1
    # end_index = -1
    # for idx, element in enumerate(unsorted_list[:-1]):
    #     if unsorted_list[idx] > unsorted_list[idx+1]:
    #         start_index = idx
    #         break
    # print 'start_index'
    # print start_index
    # for idx, element in enumerate(unsorted_list[-1::-1]):
    #     if unsorted_list[-idx-1] < unsorted_list[-idx-2]:
    #         end_index = len(unsorted_list) - 1 - idx
    #         break
    # print 'end_index'
    # print end_index
    # if start_index == -1 or end_index == -1:
    #     return 0
    # max_val = max(unsorted_list[start_index:end_index+1])
    # min_val = min(unsorted_list[start_index:end_index+1])
    # print 'Min and Max Values'
    # print max_val, min_val
    # for idx, element in enumerate(unsorted_list[:start_index]):
    #     if element >= min_val:
    #         start_index = idx
    #         break
    # print unsorted_list[:end_index-1:-1]
    # print end_index
    # for idx, element in enumerate(unsorted_list[:end_index-1:-1]):
    #     print idx, element
    #     if element <= max_val:
    #         end_index = len(unsorted_list) - idx - 1
    #         break
    # return end_index - start_index + 1
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
    return len(unsorted_list) - count


def main():
    while True:
        print minConsecutiveSubArrayToSort(map(int, raw_input('Input: ').split()))


main()
