from typing import Optional,List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        oldNode = head
        prehead = ListNode(0,oldNode)

        evenPreHead : ListNode
        evenHead: ListNode = None
        while oldNode.next:
            even = oldNode.next
            if evenHead:
                evenHead.next = even
                evenHead = evenHead.next
            else:
                evenHead = even
                evenPreHead = ListNode(0,evenHead)
            oldNode.next = even.next
            if oldNode.next:
                oldNode = oldNode.next
        if evenHead:
            evenHead.next = None
            oldNode.next = evenPreHead.next
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

head = [1]
headNode = createList(head)
so = Solution()
print(so.oddEvenList(headNode))