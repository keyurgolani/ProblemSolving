def reverse_helper(sentence, start_idx, end_idx):
    for idx in range((end_idx - start_idx) / 2):
        sentence[start_idx + idx], sentence[end_idx - idx] = sentence[end_idx - idx], sentence[start_idx + idx]


def reverse_words(sentence):
    # Reverse everything
    reverse_helper(sentence, 0, len(sentence) - 1)
    # Reverse each word
    start_idx = 0
    end_idx = 0
    for idx, char in enumerate(sentence):
        if char == ' ':
            end_idx = idx - 1
            reverse_helper(sentence, start_idx, end_idx)
            start_idx = idx + 1
    else:
        end_idx = len(sentence) - 1
        reverse_helper(sentence, start_idx, end_idx)
    return sentence


def main():
    for case in range(int(raw_input())):
        print "Case #{}: {}".format(case, ''.join(reverse_words(list(raw_input()))))


if __name__ == '__main__':
    main()
