from LinkedList import *
import copy


def main():
    head = LLNode(10)
    node2 = LLNode(20)
    node3 = LLNode(30)
    node4 = LLNode(40)
    node0 = LLNode(0)
    node10 = LLNode(100)
    ll = LinkedList(head)
    ll.append_end(node2)
    ll.append(node10)

    # node5 = LLNode(50, LLNode(60, LLNode(70, LLNode(80))))

    # ll.append_end(node5)

    # ll.append_front(node0)

    # ll.append(node3)

    # ll.append(node4, 5)

    print str(ll)

    head = LLNode(10)
    node2 = LLNode(20)
    node3 = LLNode(30)
    node4 = LLNode(40)
    node0 = LLNode(0)
    node10 = LLNode(100)

    ll2 = LinkedList()
    ll2.append_end(head)
    ll2.append_end(node2)

    node5 = LLNode(50, LLNode(60, LLNode(70, LLNode(80))))

    ll2.append_front(node5)

    # ll2.append_front(node0)

    # ll2.append_front(node5)

    # ll2.append(node3)

    # ll2.append(node4, 5)

    # ll3 = ll2

    # ll4 = copy.deepcopy(ll2)

    ll2.append_end(node10)

    # print (ll2 == ll)

    # print str(ll2 + ll)

    # del ll2[1]

    print str(ll2)

    # print str(ll3)

    # print str(ll4)

    # print (100 in ll)

    # print (100 in ll3)

    # del ll2[2:4]

    # print ll2

    # print (ll >= ll2)

    print len(ll)
    print len(ll2)

    print str(reversed(ll2))
    ll2.reverse()
    print str(ll2)

    print ll2.index(5)

    print ll2.index(50)

    ll2.remove(100)

    ll2.__setslice__(2, 4, LLNode(35, LLNode(45, LLNode(55))))

    print ll2

    ll2.map(lambda value: value * 10)

    print ll2

    for idx in range(len(ll2)):
        print ll2[idx]

    print str(ll2[2:])


if __name__ == '__main__':
    main()
