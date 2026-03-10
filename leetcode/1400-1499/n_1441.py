"""
1441. 用栈操作构建数组
"""
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        k = 0
        for i in range(1, n + 1):
            ans.append('Push')
            
            if i != target[k]:
                ans.append('Pop')
            else:
                k += 1

            if k == len(target):
                break
        return ans