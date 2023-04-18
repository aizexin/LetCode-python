from typing import List, Optional,Set
import test
import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        setpool = set()

        while head:
            if head.val in setpool:
                return head
            else:
                setpool.add(head.val)
                head = head.next

so = Solution()
so = Solution()
list1 = [1,2,4]
list2 = [1,3,4]

nodelist1 = ListNode.createList(list1)
testPrint()
