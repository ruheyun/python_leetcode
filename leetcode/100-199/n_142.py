# coding:UTF-8
# RuHe  2025/4/18 18:22
# 环形链表2
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                while slow != head:
                    slow = slow.next
                    head = head.next
                return slow
        return None