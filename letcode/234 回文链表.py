from typing import Optional,List
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temphead = head
        stack = list()
        
        while temphead:
            stack.append(temphead)
            temphead = temphead.next
        while head:
            popItem = stack.pop()
            if head.val == popItem.val :
                head = head.next
            else:
                return False
        return True
    
def createList(list: List[int])->ListNode:
    head = ListNode()
    last :ListNode = None
    for x in list:
        node = ListNode(x)
        if last:
            last.next = node
        else:
            last = node
            head = last
        last = node
    return head

head = [1,1]
headNode = createList(head)
so = Solution()
print(so.isPalindrome(headNode))