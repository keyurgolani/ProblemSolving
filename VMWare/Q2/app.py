import sys

class Elements():
    def __init__(self):
        self.values = []
        self.max = []
        self.min = []

    
    def push(self, value):
        self.values.append(value)
        if len(self.min) > 0:
            if value <= self.min[-1]:
                self.min.append(value)
        else:
            self.min.append(value)
        if len(self.max) > 0:
            if value >= self.max[-1]:
                self.max.append(value)
        else:
            self.max.append(value)

    
    def pop(self, value):
        self.values.remove(value)
        try:
            self.max.remove(value)
            self.min.remove(value)
        except ValueError:
            pass

    def minmaxproduct(self):
        try:
            if len(self.min) > 0 and len(self.max) > 0:
                return self.max[-1] * self.min[-1]
            else:
                return min(self.values) * max(self.values)
        except:
            return 1
    

def solution(operations, values):
    elements = Elements()
    for operation, value in zip(operations, values):
        if operation == "push":
            elements.push(value)
        elif operation == "pop":
            elements.pop(value)
        else:
            pass
        print elements.minmaxproduct()


def main():
    count = int(raw_input())
    operations = []
    values = []
    for idx in xrange(count):
        operations.append(raw_input())
    count2 = int(raw_input())
    for idx in xrange(count2):
        values.append(int(raw_input()))
    solution(operations, values)


if __name__ == "__main__":
    main()
