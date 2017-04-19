def answer(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 1
    elif num == 3:
        return 2
    else:
        return answer(num // 4) + answer(num % 4)

print(answer(2147483647))
