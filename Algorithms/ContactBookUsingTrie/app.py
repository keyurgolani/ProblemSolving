class TrieNode(object):
    def __init__(self, children={}, bucket=None, end=False):
        self._children = children
        self._bucket = bucket
        self._end = end

    @property
    def children(self):
        return self._children

    @property
    def bucket(self):
        return self._bucket


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert_key(self, key, value):
        current_node = self.root
        for char in key:
            if char not in current_node.children.keys():
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node._bucket = value
        current_node._end = True

    def __contains__(self, key):
        return self._has_key(key)

    def _has_key(self, key):
        current_node = self.root
        for char in key:
            if char not in current_node.children.keys():
                return False
            else:
                current_node = current_node.children[char]
        else:
            return True

    def retrieve_val(self, key):
        current_node = self.root
        for char in key:
            if char not in current_node.children.keys():
                return None
            else:
                current_node = current_node.children[char]
        else:
            return current_node._bucket

    def start_with_prefix(self, prefix):
        # TODO: Still don't understand it. Need to implement
        # values = []
        # current_node = self.root
        # for char in prefix:
        #     if char in current_node.children.keys():
        #         current_node = current_node.children[char]
        # for char, child in current_node.children.items():
        #     next_str = char
        #     while child
        pass


def main():
    contact_book = Trie()
    for case in range(int(raw_input())):
        name, number = raw_input().split()
        contact_book.insert_key(name, number)
    while True:
        try:
            name = raw_input()
            if name in contact_book:
                print "{}'s phone number is {}".format(
                    name, contact_book.retrieve_val(name))
            else:
                print "Contact Book does not have {}'s contact details".format(
                    name)
        except EOFError:
            break


if __name__ == '__main__':
    main()
