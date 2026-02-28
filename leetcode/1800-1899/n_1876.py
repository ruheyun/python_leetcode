"""
1876. 长度为三且各字符不同的子字符串
"""
from collections import Counter


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 2):
            cnt = Counter(s[i:i+3])
            if len(cnt) == 3:
                ans += 1
        return ans


print(Solution().countGoodSubstrings("xyzzaz"))