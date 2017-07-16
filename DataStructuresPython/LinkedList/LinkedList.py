class LLNode(object):
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

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

    def append(self, node, position=None):
        if position is None or position == 0:
            self.append_front(node)
        else:
            current_node = self._head
            for _ in range(position - 1):
                current_node = current_node.next
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
        pass
