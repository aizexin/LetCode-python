from typing import Optional,List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(0,head)
        oldNode = head
        evenNode = oldNode.next
        while evenNode:
            oldNode.next = evenNode.next
            oldNode = oldNode.next
            oldNode.next = evenNode
            evenNode.next = oldNode.next
            evenNode = evenNode.next
        return prehead.next
    
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

head = [1,2,3,4,5]
headNode = createList(head)
so = Solution()
print(so.oddEvenList(headNode))