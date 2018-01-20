def pretty_print_tree(root):
    treeString = ""
    maxDepth = findMaxDepth(root)
    nodeList = convertToNodeList(root)
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
    print treeString


def convertToNodeList(root):
    maxDepth = findMaxDepth(root)
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


def findMaxDepth(root):
    if root == None or root.value == None:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left:
        return findMaxDepth(root.right) + 1
    elif not root.right:
        return findMaxDepth(root.left) + 1
    else:
        return max(findMaxDepth(root.right), findMaxDepth(root.left)) + 1