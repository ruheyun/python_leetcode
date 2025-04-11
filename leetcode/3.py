# coding:UTF-8
# RuHe  2025/4/11 23:44
# 无重复字符的最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_max = len(set(s))
        if str_max < 3:
            return str_max
        ans = l =  0
        w = set()
        for r, c in enumerate(s):
            while c in w:
                w.remove(s[l])
                l += 1
            w.add(c)
            ans = max(ans, r - l + 1)
        return ans
