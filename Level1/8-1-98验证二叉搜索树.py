from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        array = list()
        # 中序遍历
        def LNR(node: Optional[TreeNode]):
            if node == None:
                return
            LNR(node.left)
            array.append(node.val)
            LNR(node.right)
        LNR(root)
        # 判断是否为升序
        count = len(array)
        if count <= 1:
            return True
        index = 1
        
        while index < count:
            if array[index] <= array[index -1]:
                return False
            index += 1
        return True
    
node5 = TreeNode(5)
node4 = TreeNode(4)
node6 = TreeNode(6)
node3 = TreeNode(3)
node7 = TreeNode(7)
node5.left = node4
node5.right = node6
node6.left = node3
node6.right = node7
so = Solution()
print(so.isValidBST(node5))