from BinaryTree import BinaryTree
from BinaryTree import Node as BTNode
from Stack import Stack
from Stack import Node as SNode


def path_to_root(root, value):
    if root == None:
        return None
    if root.value == value:
        return Stack(head=SNode(value=root))
    left_path = path_to_root(root.left, value)
    if left_path != None:
        left_path.push(root)
        return left_path
    right_path = path_to_root(root.right, value)
    if right_path != None:
        right_path.push(root)
        return right_path
    return None


def LCA(root, value1, value2):
    path1 = path_to_root(root, value1)
    path2 = path_to_root(root, value2)
    current_node1 = path1.pop
    current_node2 = path2.pop
    lca = current_node1
    while current_node2.value == current_node1.value:
        lca = current_node1
        current_node1 = path1.pop
        current_node2 = path2.pop
    return lca.value


def main():
    bt = BinaryTree(root=BTNode(20, left=BTNode(8, left=BTNode(4), right=BTNode(12, left=BTNode(10), right=BTNode(14))), right=BTNode(22)))
    print "LCA: {}".format(LCA(bt.root, 4, 14))


if __name__ == '__main__':
    main()
