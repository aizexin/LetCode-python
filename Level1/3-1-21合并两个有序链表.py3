from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        index = 0        
        while list1 or list2:

            if list1 != None and list2 != None:
                tempNode : ListNode
                if list1.val < list2.val:
                    tempNode = ListNode(list1.val)
                    list1 = list1.next
                elif list2.val <= list1.val:
                    tempNode = ListNode(list2.val)
                    list2 = list2.next

                if index == 0:
                    head = tempNode
                    lastNode = head
                else:
                    lastNode.next = tempNode
                    lastNode = tempNode

            elif list1 == None:
                lastNode.next = list2
                break
            elif list2 == None:
                lastNode.next = list1
                break

            index = index + 1
        return head
    
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

so = Solution()
list1 = [1,2,4]
list2 = [1,3,4]

nodelist1 = createList(list1)
nodelist2 = createList(list2)
# showList(nodelist1)
showList(so.mergeTwoLists(nodelist1, nodelist2))