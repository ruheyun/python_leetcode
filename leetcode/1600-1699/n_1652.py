"""
1652. 拆炸弹
"""
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        cnt = [0] * n
        if k > 0:
            for i in range(n):
                cnt[i] = sum(code[i + 1:k + i + 1]) if k + i + 1 <= n else sum(code[i + 1:n]) + sum(code[0:k - (n - i -1)])
        elif k < 0:
            for i in range(n):
                cnt[i] = sum(code[i + k:i]) if i + k >= 0 else sum(code[0:i]) + sum(code[n + (k + i):n])
        return cnt
    

sol = Solution()
result = sol.decrypt([2,4,9,3], -2)
print(result)