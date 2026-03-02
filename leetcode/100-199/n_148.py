# 排序链表
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass



lst = [4, 2, 1, 3]

head = tail = ListNode(lst[0])
for i in range(1, len(lst)):
    node = ListNode(lst[i])
    tail.next = node
    tail = node

sol = Solution()
headSort = sol.sortList(head)
for x in headSort:
    pass
