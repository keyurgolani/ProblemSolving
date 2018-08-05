from itertools import permutations

def Solution(digits):
    max_allowed_hh = 23
    max_allowed_mm = 59
    max_hh_so_far = -1
    max_mm_so_far = -1
    for permutation in permutations(digits):
        hh = int(str(permutation[0]) + str(permutation[1]))
        mm = int(str(permutation[2]) + str(permutation[3]))
        if hh < max_allowed_hh and mm < max_allowed_mm:
            if hh > max_hh_so_far or (hh == max_hh_so_far and mm > max_mm_so_far):
                max_hh_so_far = hh
                max_mm_so_far = mm
    return "{}:{}".format(max_hh_so_far, max_mm_so_far)
        

def main():
    for line in sys.stdin:
        digits = map(int, line.split(' '))
        print Solution(digits)


if __name__ == '__main__':
    main()


