from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    a = list()
    def preorder(self, root: 'Node') -> List[int]:
        p = root
        if p == None:
            return a
        self.a.append(p.val)
        for child in p.children:
            self.preorder(child)
        return self.a
    
