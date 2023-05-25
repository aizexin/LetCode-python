from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    a = list()
    def preorder(self, root: 'Node') -> List[int]:
        a = []
        
        def dps(root):
            if root == None:
                return a
            a.append(root.val)
            for child in root.children:
                dps(child)
        dps(root)

        return a
    
