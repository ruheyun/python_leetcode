"""
1763. 最长的美好子字符串
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''
        for i, c in enumerate(s):
            if c.upper() not in s or c.lower() not in s:
                return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key=len)
        return s