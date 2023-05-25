from typing import List, Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if p == root:
            return p
        elif q == root:
            return q
        # 获取路经
        def getPath(root :TreeNode, target:TreeNode)->List:
            path = list()
            while root != None:
                path.append(root)
                if root.val < target.val:
                    root = root.right
                elif root.val == target.val:
                    break
                else:
                    root = root.left
            return path
        path1 = getPath(root, p)
        path2 = getPath(root, q)
        # 找到第一个分歧点
        count = max(len(path1),len(path2))
        index = 0
        while index < count:
            if len(path1) <= index:
                return path1[index -1]
            if len(path2) <= index:
                return path2[index -1]
            if path1[index] == path2[index]:
                index += 1
            else:
                return path1[index -1]

node6 = TreeNode(6)
node2 = TreeNode(2)
node8 = TreeNode(8)
node0 = TreeNode(0)
node4 = TreeNode(4)
node7 = TreeNode(7)
node9 = TreeNode(9)
node5 = TreeNode(5)
node3 = TreeNode(3)

node6.left = node2
node6.right = node8
node2.left = node0
node2.right = node4
node8.left  = node7
node8.right = node9
node4.left = node3
node4.right = node5

so = Solution()
node = so.lowestCommonAncestor(node6, node2, node4)
print(node.val)