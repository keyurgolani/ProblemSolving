def merge_lists(l, r):
    merged_list = []
    while len(l) or len(r):
        if len(l) and len(r):
            if l[0] < r[0]:
                merged_list.append(l[0])
                del l[0]
            else:
                merged_list.append(r[0])
                del r[0]
        elif len(l):
            merged_list.append(l[0])
            del l[0]
        elif len(r):
            merged_list.append(r[0])
            del r[0]
    return merged_list

def merge_sort(input):
    if len(input) > 1:
        return merge_lists(merge_sort(input[:len(input)/2]), merge_sort(input[len(input)/2:]))
    else:
        return input


def main():
    print merge_sort(map(int, raw_input().split()))


main()
