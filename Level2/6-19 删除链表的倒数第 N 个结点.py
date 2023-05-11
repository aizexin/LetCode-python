from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rightNode = head
        res =  ListNode(0,head)
        leftNode = res
        index = 0
        while rightNode:
            if index < n:
                rightNode = rightNode.next
            else:
                leftNode = leftNode.next
                rightNode = rightNode.next
            index += 1
        if index == 1:
            return None
        leftNode.next = leftNode.next.next
        return res.next