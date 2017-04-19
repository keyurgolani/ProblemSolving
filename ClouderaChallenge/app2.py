ordinals = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10
}


def getOrderNumber(order):
    number = 0
    if 'L' in order:
        number += 50
        for negative_element in order[:order.index('L')]:
            number -= ordinals[negative_element]
        for positive_element in order[order.index('L') + 1:]:
            number += ordinals[positive_element]
    elif 'X' in order:
        for negative_element in order[:order.index('X')]:
            number -= ordinals[negative_element]
        for positive_element in order[order.index('X'):]:
            number += ordinals[positive_element]
    elif 'V' in order:
        for negative_element in order[:order.index('V')]:
            number -= ordinals[negative_element]
        for positive_element in order[order.index('V'):]:
            number += ordinals[positive_element]
    else:
        number = len(order)
    return number


def compareRomanNames(name):
    first_name, order = name.split(" ")
    return (first_name, getOrderNumber(order))


def answer(names):
    names.sort(key=compareRomanNames)
    return names


def main():
    names = []
    for _ in range(int(raw_input())):
        names.append(raw_input())
    for name in answer(names):
        print name


if __name__ == '__main__':
    main()
