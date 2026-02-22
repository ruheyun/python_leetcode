"""
28. 找出字符串中第一个匹配项的下标
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        for i in range(len(haystack)):
            if h < n or h - i < n:
                break
            j = i
            for x in needle:
                if x != haystack[j]:
                    break
                j += 1
            if j - i == len(needle):
                return i
        return -1
    
    def strStr_(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1

