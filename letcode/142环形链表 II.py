# Definition for singly-linked list.
from typing import Optional, Set,List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def print(self):
        while self:
            print(self.val + '->'),
            self = self.next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        setPool = set()
        while head:
            if head in setPool:
                return head
            else:
                setPool.add(head)
            head = head.next

def createCycleList(list :List, pos):
    
    index = 0
    preNode :ListNode
    headNode :ListNode
    for value in list:
        node = ListNode(value)
        if index == 0:
            preNode = node
            headNode = node
        else:
            preNode.next = node
        preNode = node
        index = index + 1
    
    index2 = 0
    tempHead =  headNode
    while tempHead:
        if pos == index2:
            preNode.next = tempHead
            break
        tempHead = tempHead.next
        index2 = index2 + 1
    return headNode

so = Solution()
list = [-1,-7,7,-4,19,6,-9,-5,-2,-5]
head = createCycleList(list, 6)
print(so.detectCycle(head).val)
    
# ---------示例代码------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast: # 因为fast比slow快, 如果不存在环, 只需判断fast是否为空即可
            slow = slow.next
            if fast.next == None: return None
            fast = fast.next.next
            if slow == fast: break # 不能写到while循环的判断条件中, 因为初始slow=head,会无法进入循环, java可以用do{}while;
        if fast == None: return None # 因为fast比slow快, 如果不存在环, 只需判断fast是否为空即可
        # 设a为head到环入口的距离, b为环入口到相遇位置的距离, c为相遇位置到环入口的距离, 
        # 即b+c是环的长度, n为两个指针首次相遇时, 快指针走完的环的圈数, 慢指针显然只能一圈也未走完
        # 根据快指针移动距离为慢指针的两倍, 有如下式子
        # 2(a + b) = a + n(b + c) + b
        # 解出 a = nc + nb - b = (n-1)(b+c) + c
        # 因此让一个新的指针指向head ,每次走一步,走完距离a到达环入口, 
        # 另外一个指针也每次走一步, 出发位置为快慢指针的首次相遇位置, 也走距离a, 
        # 因为其离环入口的距离为c, 因为a % 环长n = c, 走完距离a必定可以到达环入口 , 
        # 这样两个新的慢指针相遇位置即为环的入口
        slow = head # fast = head也一样
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    