"""
1461. 检查一个字符串是否包含所有长度为 K 的二进制子串
"""
from collections import defaultdict


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cnt = defaultdict(int)
        for i in range(len(s)):
            left = i - k + 1
            if left >= 0:
                cnt[s[left:i + 1]] += 1
                if len(cnt) == 2 ** k:
                    return True
        return False


sol = Solution()
result = sol.hasAllCodes("0110", 2)
print(result)