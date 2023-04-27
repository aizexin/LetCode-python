from typing import Deque, List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 用数组，层次遍历创建树
def createTree(array: list)-> TreeNode:
    index = 0
    deque = Deque()
    rootNode = TreeNode(array[index])
    deque.append(rootNode)
    index = 1
    while deque:
        node = deque.popleft()

        if node == None:
            index += 2
            continue
        if index < len(array):
            if array[index] == None:
                deque.append(None)
            else:
                LeftNode = TreeNode(array[index])
                node.left = LeftNode
                deque.append(LeftNode)
            index += 1
        if index < len(array):
            if array[index] == None:
                deque.append(None)
            else:
                RightNode = TreeNode(array[index])
                node.right = RightNode
                deque.append(RightNode)
            index += 1
    return rootNode

# 层次遍历显示
def showTreeHierarchcalTravel(rootNode: Optional[TreeNode]):
    deque = Deque()
    showList = list()
    if rootNode:
        deque.append(rootNode)
    else:
        return
    while deque:
        node :Optional[TreeNode] = deque.popleft()
        if node != None:
            showList.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        else:
            showList.append(None)
    
    print(showList)