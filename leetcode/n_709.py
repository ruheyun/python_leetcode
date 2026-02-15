"""
Docstring for leetcode.n_709 转换成小写字母
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
    
    def toLowerCase_(self, s: str) -> str:
        ans = ''
        for c in s:
            c_int = ord(c)
            if c_int >= 65 and c_int <= 90:
                ans += chr(c_int + 32)
            else:
                ans += c
        return ans
    
