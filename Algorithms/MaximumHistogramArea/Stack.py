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
    def __init__(self, head_value=None):
        self._head = Node(value=head_value)
        self._size = 0 if head_value == None else 1

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

    def __str__(self):
        _str = ""
        current_node = self._head
        while current_node != None:
            # Change _str += str(current_node.value.value)
            # to
            # _str += str(current_node.value)
            # in case of other raw format data like int
            _str += str(current_node.value)
            if current_node._next != None:
                _str += " --> "
            current_node = current_node._next
        return _str
