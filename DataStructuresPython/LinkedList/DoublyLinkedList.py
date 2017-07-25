class DLLNode(object):
    def __init__(self, value=None):
        self._value = value
        self._next = None
        self._previous = None

    def __del__(self):
        self._next = None
        self._previous = None
        del self._value

    def __delete__(self):
        self.__del__()

    def __deepcopy__(self, memodict={}):
        other = type(self)(self._value)
        return other

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @value.getter
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @next.setter
    def next(self, next):
        self._next = next

    @next.getter
    def next(self):
        return self._next

    @previous.setter
    def previous(self, previous):
        self._previous = previous

    @previous.getter
    def previous(self):
        return self._previous

    def __str__(self):
        node_string = '= [ ' + str(self._value) + ' ] ='
        if self.previous is None:
            node_string = '[Start] <-' + node_string
        if self._next is None:
            node_string += '-> [END]'
        return node_string


class DoublyLinkedList(object):
    def __init__(self, head=None):
        self._head = head
        self._tail = head
        if head is not None:
            self._length = 1
        else:
            self._length = 0

    def __str__(self):
        ll_string = ''
        current_node = self._head
        while current_node is not None:
            ll_string += str(current_node)
            current_node = current_node.next
        return ll_string

    def __len__(self):
        return self._length

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value):
        self._head = value.head
        self._tail = value.tail
        self._length = value.length

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        self._head = head

    @head.getter
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, tail):
        self._tail = tail

    @tail.getter
    def tail(self):
        return self._tail

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @length.getter
    def length(self):
        return self._length

    def append_end(self, node):
        self._tail.next = node
        node.previous = self._tail
        self._tail = self._tail.next
        self._length += 1

    def append_front(self, node):
        self._head.previous = node
        node.next = self._head
        self._head = self._head.previous
        self._length += 1

    def append(self, node, key=None):
        if key is None:
            self.append_end(node)
        else:
            if key > self._length or key < 0:
                raise IndexError('Index ' + str(key) + ' out of range')
            else:
                current_node = None
                if key > self._length / 2:
                    current_node = self._tail
                    for _ in range(self._length - key):
                        current_node = current_node.previous
                else:
                    current_node = self._head
                    for _ in range(key - 1):
                        current_node = current_node.next
                current_node.next.previous = node
                node.next = current_node.next
                current_node.next = node
                node.previous = current_node
                self._length += 1
