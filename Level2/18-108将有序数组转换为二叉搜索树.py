from typing import Optional, List
from CommonFunction.TreeFunction import createTree, showTreeHierarchcalTravel
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 通过二分查找的思想创建树
        def midCreateTreeNode(array, leftIndex, rightIndex):
            if leftIndex >  rightIndex:
                return
            midIndex = (rightIndex - leftIndex) // 2 + leftIndex
            node = TreeNode(array[midIndex])
            node.left = midCreateTreeNode(array, leftIndex, midIndex - 1)
            node.right = midCreateTreeNode(array ,midIndex + 1, rightIndex)
            return node
        return midCreateTreeNode(nums,0, len(nums)-1)
        
so = Solution()
nums = [-10,-3,0,5,9]
# tree = createTree(nums)
# showTreeHierarchcalTravel(tree)
showTreeHierarchcalTravel(so.sortedArrayToBST(nums))

