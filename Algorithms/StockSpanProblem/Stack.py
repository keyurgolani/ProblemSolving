class Node(object):
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next


class Stack(object):
    def __init__(self, head=None):
        self._head = head
        self._size = 0

    def push(self, value):
        self._head = Node(value=value, next=self._head)
        self._size += 1

    @property
    def top(self):
        return self._head.value

    @property
    def pop(self):
        if self._head is None:
            return None
        current_node = self._head
        self._head = self._head.next
        value = current_node.value
        del current_node
        self._size -= 1
        return value

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self._size == 0
