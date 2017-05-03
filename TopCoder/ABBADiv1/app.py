class ABBADiv1(object):
    def OP1(self, input):
        return input + 'A'

    def OP2(self, input):
        return 'B' + input[::-1]

    def canObtain(self, input, target):
        if input == target:
            return 'Possible'
        if input not in target and input[::-1] not in target:
            return 'Impossible'
        if len(input) >= len(target):
            return 'Impossible'
        if self.canObtain(self.OP1(input), target) == 'Possible' or self.canObtain(self.OP2(input), target) == 'Possible':
            return 'Possible'
        else:
            return 'Impossible'


def main():
    abbadiv1 = ABBADiv1()
    for case in range(int(raw_input())):
        input, target = raw_input().split()
        print "Case #{}: {}".format(case, abbadiv1.canObtain(input, target))


if __name__ == '__main__':
    main()
