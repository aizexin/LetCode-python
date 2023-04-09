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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rehead = self.reverse(None, head)
        return rehead
    
    def reverse(self, pre: Optional[ListNode], current: ListNode) -> ListNode:
        if current == None:
            return pre
        else:
            next = current.next
            current.next = pre
            return self.reverse(current, next)
        
            

so = Solution()
list1 = [1,2,4]

nodelist1 = createList(list1)
newhead   = so.reverseList(nodelist1)
showList(newhead)
