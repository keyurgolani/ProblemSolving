class LLNode(object):
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def __del__(self):
        del self._value
        del self._next

    def __delete__(self):
        del self._value
        del self._next

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

    @next.setter
    def next(self, next):
        self._next = next

    @next.getter
    def next(self):
        return self._next

    def __str__(self):
        node_string = '[ ' + str(self._value) + ' ] --> '
        if self._next is None:
            node_string += '[END]'
        return node_string


class LinkedList(object):
    def __init__(self, head=None):
        self._head = head
        self._current_node = self._head

    def __str__(self):
        ll_string = ''
        current_node = self._head
        while current_node is not None:
            ll_string += str(current_node)
            current_node = current_node.next
        return ll_string

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value):
        self._head = value.head

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        self._head = head

    @head.getter
    def head(self):
        return self._head

    def append_end(self, node):
        if self._head is None:
            self._head = node
        else:
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def append_front(self, node):
        node_first = node
        node_last = node
        while node_last.next is not None:
            node_last = node_last.next
        node_last.next = self._head
        self._head = node_first

    def append(self, node, key=None):
        if key is None or key == 0:
            self.append_front(node)
        else:
            current_node = self._head
            try:
                for _ in range(key - 1):
                    current_node = current_node.next
            except AttributeError:
                raise IndexError('Index ' + str(key) + ' out of range')
            node_first = node
            node_last = node
            while node_last.next is not None:
                node_last = node_last.next
            node_last.next = current_node.next
            current_node.next = node_first

    def __del__(self):
        if self._head is None:
            return
        else:
            current_node = self._head
            while current_node is not None:
                del_node = current_node
                current_node = current_node.next
                del del_node

    def __delete__(self):
        if self._head is None:
            return
        else:
            current_node = self._head
            while current_node is not None:
                del_node = current_node
                current_node = current_node.next
                del del_node

    def __copy__(self):
        return type(self)(self._head)

    def __deepcopy__(self, memodict={}):
        other = type(self)()
        if self._head is not None:
            current_node = self._head
            other.append_front(LLNode(current_node.value))
            current_new_node = other.head
            current_node = current_node.next
            while current_node is not None:
                other.append_end(LLNode(current_node.value))
                current_node = current_node.next
                current_new_node = current_new_node.next
        return other

    def __add__(self, other):
        if other.head is None:
            return self.__deepcopy__()
        elif self._head is None:
            return other.__deepcopy__()
        else:
            new = type(self)()
            new_self = self.__deepcopy__()
            new_other = other.__deepcopy__()
            new.append_end(new_self.head)
            new.append_end(new_other.head)
            return new

    def __cmp__(self, other):
        if (other.head is None and self._head is not None) or (other.head is not None and self._head is None):
            return False
        else:
            self_ptr = self._head
            other_ptr = other.head
            while self_ptr is not None and other_ptr is not None:
                if self_ptr.value != other_ptr.value:
                    return False
                else:
                    self_ptr = self_ptr.next
                    other_ptr = other_ptr.next
            if self_ptr is not None or other_ptr is not None:
                return False
            else:
                return True

    def __compare__(self, other, greater, less, equal):
        if self._head is None and other.head is None:
            return True if equal else False
        elif self._head is None and other.head is not None:
            return True if less else False
        elif self._head is not None and other.head is None:
            return True if greater else False
        else:
            self_ptr = self._head
            other_ptr = other.head
            while self_ptr is not None and other_ptr is not None and self_ptr.value == other_ptr.value:
                self_ptr = self_ptr.next
                other_ptr = other_ptr.next
            if self_ptr is None and other_ptr is None:
                return True if equal else False
            elif self_ptr is None and other_ptr is not None:
                return True if less else False
            elif self_ptr is not None and other_ptr is None:
                return True if greater else False
            else:
                if self_ptr.value > other_ptr.value:
                    return True if greater else False
                elif self_ptr.value < other_ptr.value:
                    return True if less else False
                else:
                    return True if equal else False

    def __ge__(self, other):
        return self.__compare__(other, True, False, True)

    def __le__(self, other):
        return self.__compare__(other, False, True, True)

    def __gt__(self, other):
        return self.__compare__(other, True, False, False)

    def __lt__(self, other):
        return self.__compare__(other, False, True, False)

    def __eq__(self, other):
        return self.__compare__(other, False, False, True)

    def __ne__(self, other):
        return not self.__compare__(other, False, False, True)

    def __contains__(self, item):
        if self._head is None:
            return False
        else:
            current_node = self._head
            while current_node is not None:
                if current_node.value == item:
                    return True
                else:
                    current_node = current_node.next
            else:
                return False

    def __delitem__(self, key):
        if self._head is None:
            return False
        else:
            current_node = self._head
            try:
                for _ in range(key - 1):
                    current_node = current_node.next
            except AttributeError:
                raise IndexError('Index ' + str(key) + ' out of range')
            del_node = current_node.next
            current_node.next = del_node.next
            del del_node
            return True

    def __delslice__(self, i, j):
        if self._head is None:
            return False
        else:
            node_before_slice = self._head
            try:
                for _ in range(i - 1):
                    node_before_slice = node_before_slice.next
            except AttributeError:
                raise IndexError('Index ' + str(i) + ' out of range')
            slice_first_node = node_before_slice.next
            node_after_slice = slice_first_node
            try:
                for _ in range(j - i):
                    node_after_slice = node_after_slice.next
            except AttributeError:
                raise IndexError('Index ' + str(j) + ' out of range')
            node_after_slice = slice_first_node
            for _ in range(j - i):
                del_node = node_after_slice
                node_after_slice = node_after_slice.next
                del del_node
            node_before_slice.next = node_after_slice
            return True

    def __len__(self):
        if self._head is None:
            return 0
        else:
            current_node = self._head
            length = 0
            while current_node is not None:
                current_node = current_node.next
                length += 1
            return length

    def reverse(self):
        if self._head is None or self._head.next is None:
            return
        else:
            current_node = self._head
            previous_node = None
            next_node = self._head.next
            while current_node is not None:
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
                if current_node is not None:
                    next_node = current_node.next
            self._head = previous_node

    def __reversed__(self):
        other = self.__deepcopy__()
        other.reverse()
        return other

    def __setitem__(self, key, value):
        self.append(value, key)

    def __setslice__(self, i, j, sequence):
        if self._head is None:
            return False
        else:
            node_before_slice = self._head
            try:
                for _ in range(i - 1):
                    node_before_slice = node_before_slice.next
            except AttributeError:
                raise IndexError('Index ' + str(i) + ' out of range')
            slice_first_node = node_before_slice.next
            node_after_slice = slice_first_node
            try:
                for _ in range(j - i):
                    node_after_slice = node_after_slice.next
            except AttributeError:
                raise IndexError('Index ' + str(j) + ' out of range')
            node_after_slice = slice_first_node
            sequence_last_node = sequence
            while sequence_last_node.next is not None:
                sequence_last_node = sequence_last_node.next
            for _ in range(j - i):
                del_node = node_after_slice
                node_after_slice = node_after_slice.next
                del del_node
            node_before_slice.next = sequence
            sequence_last_node.next = node_after_slice
            return True

    def remove(self, value):
        if self._head is None:
            raise AttributeError()
        elif self._head.value == value:
            del_node = self._head
            self._head = self._head.next
            del del_node
        else:
            current_node = self._head
            try:
                while current_node.next.value != value:
                    current_node = current_node.next
            except AttributeError:
                raise AttributeError('Attribute ' + value + ' not found')
            del_node = current_node.next
            current_node.next = del_node.next
            del del_node

    def index(self, value):
        if self._head is None:
            return -1
        else:
            current_node = self._head
            idx = 0
            try:
                while current_node.value != value:
                    idx += 1
                    current_node = current_node.next
            except AttributeError:
                return -1
            return idx

    def map(self, func):
        if self._head is None:
            return
        current_node = self._head
        while current_node is not None:
            current_node.value = func(current_node.value)
            current_node = current_node.next

