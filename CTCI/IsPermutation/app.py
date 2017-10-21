# Simple check for anagram strings.
# Anagram strings are the strings that have the same characters in different
# permutation.
# Time Complexity for the code is O(n) because we iterate the length of input
# at most 3 times, once with the first string, once with second string and
# once with summing remaining occurrances in the lookup. However, this depends
# on the size of the input only linearly.
# Space Complexity for the code is O(n) because we store lookup of maximum the
# size of the input.


def solution(string1, string2):
    lookup = {}
    if len(string1) != len(string2):
        return False
    for char in string1:
        try:
            lookup[char] += 1
        except KeyError:
            lookup[char] = 1
    for char in string2:
        try:
            if lookup[char] == 0:
                return False
            lookup[char] -= 1
        except KeyError:
            return False
    if sum(lookup.values()) == 0:
        return True
    else:
        return False



def main():
    for idx in xrange(int(raw_input())):
        print "Case #{}: {}".format(idx, solution(*raw_input().split(" ")))

# Run with `cat input.in | python app.py`
if __name__ == '__main__':
    main()
