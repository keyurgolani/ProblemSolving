class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self._value = value
        self._left = left
        self._right = right

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right


class BinaryTree(object):
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root
