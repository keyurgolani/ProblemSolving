# Given a string, check if every character in the string exists only once
# Time Complexity O(n) because in the worst case the input is all possible
# ascii characters and we will have to traverse through all of them before
# deciding the result.
# Space Complexity is O(1) because we use constant space.
# Note: Actually the space complexity should be O(n) because in worst case
# we have all 128 ascii characters once in the input and we use space equal to
# the input size.
# Note: Also in a way, you can say that the time complexity is constant because
# however big the input gets, if it is more than 128 chars, we return instantly
# meaning that the time complexity of our execution is capped at processing
# the input of 128 characters. Doesn't depend on the input size technically.

def solution(string):
    # Constrainting the string to be an ascii string rather than unicode or
    # other encoding
    if len(string) > 128:
        # Total only 128 unique characters possible.
        return False

    # Lookup for all possible ascii characters. Calls for O(1) space because
    # however big the input gets, the lookup size will remain the same.
    lookup = [False] * 128
    for char in string:
        index = ord(char)
        if lookup[index]:
            return False
        lookup[index] = True
    return True

def solution2(string):
    # Constrainting the string to be an ascii string rather than unicode or
    # other encoding
    if len(string) > 128:
        # Total only 128 unique characters possible.
        return False

    return len(string) == len(set(string))

def solution3(string):
    # Constrainting the string to be an ascii string rather than unicode or
    # other encoding
    if len(string) > 128:
        # Total only 128 unique characters possible.
        return False

    for char in string:
        if string.count(char) > 1:
            return False
    return True

def main():
    for idx in xrange(int(raw_input())):
        print "Case #{}: {}".format(idx, solution(raw_input()))


# Run with `cat input.in | python app.py`
if __name__ == '__main__':
    main()
