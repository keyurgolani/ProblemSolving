class AB(object):

    def createABString(self, arr, pairs, target, b_count, idx):
        if pairs == target:
            return arr
        if idx == len(arr):
            return None
        new_arr = arr[:]
        without_flipping_current_idx = self.createABString(new_arr, pairs, target, b_count, idx + 1)
        if without_flipping_current_idx is not None:
            return without_flipping_current_idx
        if idx > int(len(arr) / 2):
            new_arr[idx] = 'B'
            with_flipping_current_idx = self.createABString(new_arr, pairs + idx - b_count, target, b_count + 1, idx + 1)
            if with_flipping_current_idx is not None:
                return with_flipping_current_idx
        return None

    def createString(self, length, target_pairs):
        if int(length / 2) * length - int(length / 2) < target_pairs:
            return ''
        else:
            working_str = ['A'] * length
            result = self.createABString(working_str, 0, target_pairs, 0, 0)
            if result is None:
                return ''
            else:
                return ''.join(result)


def main():
    ab = AB()
    for case in range(int(raw_input())):
        length, pairs = map(int, raw_input().split())
        print "Case #{}: {}".format(case, ab.createString(length, pairs))


if __name__ == '__main__':
    main()
