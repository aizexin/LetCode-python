from typing import Optional,Deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def hightForTree(rootNode, depth) -> int:
            if rootNode == None:
                return depth
            else:
                depth += 1
            left = hightForTree(rootNode.left, depth )
            right = hightForTree(rootNode.right, depth)
            return max( left,right)
            # if rootNode.left:
            #     hightForTree(rootNode.left, depth + 1)
            # if rootNode.right:
            #     hightForTree(rootNode.right, depth + 1)
        if root == None:
            return True
        else:
            hightL = hightForTree(root.left, 0)
            hightR = hightForTree(root.right, 0)
            return abs(hightR - hightL) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

        
    
# def createTree(array: list)-> TreeNode:
#     index = 0
#     deque = Deque()
#     rootNode = TreeNode(array[index])
#     deque.append(rootNode)
#     index += 1
#     while deque:
#         node = deque.popleft()
#         if index < len(array) and array[index] != -1:
#             LeftNode = TreeNode(array[index])
#             node.left = LeftNode
#             deque.append(LeftNode)
#             index += 1
#         if index < len(array) and array[index] != -1:
#             RightNode = TreeNode(array[index])
#             node.right = RightNode
#             deque.append(RightNode)
#             index += 1
#     return rootNode

# array = [1,2,2,3,-1,-1,3,4,-1,-1,4]
# rootNode = createTree(array)
# so = Solution()
# print(so.isBalanced(rootNode))
    
        