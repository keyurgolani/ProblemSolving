def  getMinimumUniqueSum(arr):
    sum = 0
    result = []
    for idx, element in enumerate(arr):
        if element == arr[idx - 1]:
            while element in result:
                element += 1
            else:
                sum += element
                result.append(element)
        else:
            sum += element
            result.append(element)
    return sum


def main():
    N = int(raw_input())
    values = []
    for _ in xrange(N):
        values.append(int(raw_input()))
    print getMinimumUniqueSum(values)



main()
