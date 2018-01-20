from collections import deque
import math

class TreeNode(object):
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        if len(str(self.value)) == 1:
            return "[{}]".format(self.value if self.value is not None else " ")

class Tree(object):
    def __init__(self, root=None):
        if isinstance(root, TreeNode) or root is None:
            self.root = root
        else:
            self.root = TreeNode(root)

    def addNode(self, value):
        if value is None:
            insertNode = None
        else:
            insertNode = TreeNode(value)
        if self.root is None:
            self.root = insertNode
        else:
            minDepthPath = Tree.findMinDepthPath(self.root)
            currentNode = self.root
            for turn in minDepthPath[:-1]:
                if turn == "R":
                    currentNode = currentNode.right
                else:
                    currentNode = currentNode.left
            if minDepthPath[-1] == "R":
                currentNode.right = insertNode
            else:
                currentNode.left = insertNode

    def __str__(self):
        treeString = ""
        maxDepth = Tree.findMaxDepth(self.root)
        nodeList = Tree.convertToNodeList(self.root)
        levelNodeCount = 1
        for level in range(maxDepth):
            levelNodePositions = [((2*(n) + 1) * (2**(maxDepth - level - 1)) - 1) for n in range(levelNodeCount)]
            levelNodeCount *= 2
            for index, node in enumerate(nodeList):
                if index in levelNodePositions:
                    if node:
                        treeString += str(node)
                    else:
                        treeString += "[ ]"
                else:
                    treeString += "   "
            treeString += "\n"
        return treeString

    @staticmethod
    def convertToNodeList(root):
        maxDepth = Tree.findMaxDepth(root)
        currentDepth = 1
        def listConvertHelp(currentNode, inputList, maxDepth, currentDepth):
            if not currentNode.left and not currentNode.right:
                if currentDepth < maxDepth:
                    inputList.append(None)
                inputList.append(currentNode)
                if currentDepth < maxDepth:
                    inputList.append(None)
            else:
                if not currentNode.left:
                    inputList.append(None)
                else:
                    inputList = listConvertHelp(currentNode.left, inputList, maxDepth, currentDepth + 1)
                inputList.append(currentNode)
                if not currentNode.right:
                    inputList.append(None)
                else:
                    inputList = listConvertHelp(currentNode.right, inputList, maxDepth, currentDepth + 1)
            return inputList
        return listConvertHelp(root, [], maxDepth, currentDepth)

    @staticmethod
    def findMinDepthPath(root):
        if not root.left and not root.right:
            # If the node is leaf, new node should be appended at any position.
            # Choosing left by default.
            return ["L"]
        elif not root.right:
            return ["R"]
        elif not root.left:
            return ["L"]
        else:
            leftMinPath = Tree.findMinDepthPath(root.left)
            rightMinPath = Tree.findMinDepthPath(root.right)
            if len(leftMinPath) > len(rightMinPath):
                return ["R"] + rightMinPath
            else:
                return ["L"] + leftMinPath

    @staticmethod
    def findMaxDepth(root):
        if root == None or root.value == None:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            return Tree.findMaxDepth(root.right) + 1
        elif not root.right:
            return Tree.findMaxDepth(root.left) + 1
        else:
            return max(Tree.findMaxDepth(root.right), Tree.findMaxDepth(root.left)) + 1

    def serialize(self):
        nodeList = Tree.convertToNodeList(self.root)
        return " ".join([str(node.value) if node is not None else 'N' for node in nodeList])
    
    @staticmethod
    def deserialize(serial_tree):
        nodeList = serial_tree.split(" ")
        tree = Tree()
        maxDepth = int(math.log(len(nodeList) + 1, 2))
        level = 0
        levelNodeCount = 1
        while level < maxDepth:
            levelNodePositions = [((2*(n) + 1) * (2**(maxDepth - level - 1)) - 1) for n in range(levelNodeCount)]
            for nodePosition in levelNodePositions:
                currentNodeValue = nodeList[nodePosition]
                tree.addNode(currentNodeValue if currentNodeValue is not 'N' else None)
            level += 1
            levelNodeCount *= 2
        return tree
