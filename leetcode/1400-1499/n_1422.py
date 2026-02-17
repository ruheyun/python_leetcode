"""
Docstring for leetcode.1400-1499.n_1422 分割字符串的最大得分
"""


class Solution:
    def maxScore(self, s: str) -> int:
        ans = s.count('1')
        max_ans = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                ans += 1
            else:
                ans -= 1
            max_ans = max(max_ans, ans)
        return max_ans
        

