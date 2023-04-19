from typing import Optional,List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = head
        list = []
        while tempHead:
            list.append(tempHead.val)
            tempHead = tempHead.next
        list.sort()
        preNode :ListNode = None
        preHead :ListNode = None
        for x in list:
            node = ListNode(x)
            if preNode:
                preNode.next = node
            else:
                preNode = node
                preHead = ListNode(0,preNode)

            preNode = node
        if len(list) == 0:
            return None
        return preHead.next
    
    
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

head = []
headNode = createList(head)
so = Solution()
print(so.sortList(headNode))
        
                
            
            