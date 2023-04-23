from typing import Optional,Deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def DFSSumNumber(rootNode :Optional[TreeNode],target) -> int:
            if rootNode == None:
                return 0
            res = 0
            if rootNode.val == target:
                res += 1
            res += DFSSumNumber(rootNode.left, target - rootNode.val)
            res += DFSSumNumber(rootNode.right, target - rootNode.val)
            return res
        def DFS(node :Optional[TreeNode], targetSum) -> int:
            if node == None:
                return 0
            res = DFSSumNumber(node,targetSum)
            res += DFS(node.left ,targetSum)
            res += DFS(node.right ,targetSum)
            return res
        return DFS(root,targetSum)
    
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

array = [10,5,-3,3,2,None,11,3,-2,None,1]
rootNode = createTree(array)
so = Solution()
print(so.pathSum(rootNode ,8))