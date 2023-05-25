# Definition for a binary tree node.
from typing import Optional, List
from my_package.TreeFunction import createTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res :List = list()
        stack :List = list()
        item  :TreeNode = root
        # 迭代中序遍历
        while stack or item:
            while item:
                stack.append(item)
                item = item.left
            item = stack.pop()
            res.append(item.val)
            item = item.right           
        return res[k-1]
    

arr = [5,3,6,2,4,None,None,1]
node = createTree(arr)
so = Solution()
print(so.kthSmallest(node, 3))
    