# 两数相加
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next
        return dummy.next
    
    def second(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        while head1 and head2:
            head1 = head1.next
            head2 = head2.next
        dum = head = l1 if head1 else l2
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            head.val = carry % 10
            carry //= 10
            if carry and not head.next:
                head.next = ListNode()
            head = head.next
        return dum

