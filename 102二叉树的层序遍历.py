# Definition for a binary tree node.
from typing import Optional, List,Deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        searchDeque = Deque()
        endList = list()
        searchDeque.append(root)
        while searchDeque:
            count = len(searchDeque)
            sublist = []
            while 0 < count:
                node: TreeNode = searchDeque.popleft()
                sublist.append(node.val)
                if node.left:
                    searchDeque.append(node.left)
                if node.right:
                    searchDeque.append(node.right)
                count -= 1
            endList.append(sublist)
        return endList
    
rootNode = TreeNode(1)

so = Solution()
print(so.levelOrder(None))
    
