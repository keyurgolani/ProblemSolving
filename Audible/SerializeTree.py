from TreeModule import Tree, TreeNode

def main():
    tree = Tree()
    tree.addNode(0)
    tree.addNode(1)
    tree.addNode(2)
    tree.addNode(3)
    tree.addNode(4)
    tree.addNode(5)
    tree.addNode(6)
    tree.addNode(7)
    tree.addNode(8)
    tree.addNode(9)
    print str(tree)
    print str(Tree.deserialize(tree.serialize()))


if __name__ == '__main__':
    main()