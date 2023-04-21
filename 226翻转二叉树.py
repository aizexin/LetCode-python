from typing import Optional, Deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inverOneNode(node :Optional[TreeNode]):
            if node == None:
                return
            temp = node.left
            node.left = node.right
            node.right  = temp
            if node.left:
                inverOneNode(node.left)
            if node.right:
                inverOneNode(node.right)
          
        inverOneNode(root)
        return root
    
def createTree(array: list)-> TreeNode:
    index = 0
    deque = Deque()
    rootNode = TreeNode(array[index])
    deque.append(rootNode)
    index += 1
    while deque:
        node = deque.popleft()
        if index < len(array):
            LeftNode = TreeNode(array[index])
            node.left = LeftNode
            deque.append(LeftNode)
            index += 1
        if index < len(array):
            RightNode = TreeNode(array[index])
            node.right = RightNode
            deque.append(RightNode)
            index += 1
    return rootNode
# 层次遍历
def hierTra(root):
    deque = Deque()
    deque.append(root)
    while deque:
        node :TreeNode = deque.popleft()
        print(node.val)
        if node.left:
            deque.append(node.left)
        if node.right:
            deque.append(node.right)
        
root = [4,2,7,1,3,6,9]
rootNode = createTree(root)
so = Solution()
reverNode = so.invertTree(rootNode)
hierTra(reverNode)