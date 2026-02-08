# 两两交换链表中的结点
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(next=head)
        while cur.next and cur.next.next:
            slow = cur.next
            fast = cur.next.next
            cur.next = fast
            slow.next = fast.next
            fast.next = slow
            cur = cur.next.next
        return dummy.next
            
