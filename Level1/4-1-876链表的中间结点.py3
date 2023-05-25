# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def  createList( array: List) -> Optional[ListNode]:
    lastNode = ListNode(array[0])
    head = lastNode
    index = 1
    while index < len(array):
        item = array[index]
        node = ListNode(item)
        lastNode.next = node
        lastNode = node
        index = index + 1
    return head

def showList(head: ListNode):
    while head:
        print(head.val)
        head = head.next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lowhead = head
        fasthead = head
        while fasthead:
            lowhead = lowhead.next
            fasthead = fasthead.next
            if fasthead:
                fasthead = fasthead.next
        return lowhead


so = Solution()
list1 = [1,2,3,4,5,6]

nodelist1 = createList(list1)
print(so.middleNode(nodelist1).val)
