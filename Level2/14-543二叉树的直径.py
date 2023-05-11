from typing import Optional,Deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def depth(rootNode: Optional[TreeNode]) -> int:
            if rootNode == None:
                return 0
            leftDepth = depth(rootNode.left)
            rightDepth = depth(rootNode.right)
            nodeDepth = max(leftDepth, rightDepth) + 1
            self.res = max(self.res, leftDepth + rightDepth)
            return nodeDepth
        depth(root)
        return self.res
    
def createTree(array: list)-> TreeNode:
    index = 0
    deque = Deque()
    rootNode = TreeNode(array[index])
    deque.append(rootNode)
    index += 1
    while deque:
        node = deque.popleft()
        if index < len(array) and array[index] != -1:
            LeftNode = TreeNode(array[index])
            node.left = LeftNode
            deque.append(LeftNode)
            index += 1
        if index < len(array) and array[index] != -1:
            RightNode = TreeNode(array[index])
            node.right = RightNode
            deque.append(RightNode)
            index += 1
    return rootNode

array = [1,2]
rootNode = createTree(array)
so = Solution()
print(so.diameterOfBinaryTree(rootNode))