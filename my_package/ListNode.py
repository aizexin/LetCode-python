from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def createList(self, array: List) -> Optional[ListNode]:
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
    
    def showList(self):
        while self:
            print(self.val)
            heselfad = self.next

def testfunction():
    print('test=======')