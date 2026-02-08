# coding:UTF-8
# RuHe  2025/4/13 17:49
# 最小覆盖字串
from collections import Counter


class Solution:
    """
    给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
    如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
    """
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        cnt = Counter(t)
        cns = Counter()
        left = 0
        for right, c in enumerate(s):
            cns[c] += 1
            while cns >= cnt:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cns[s[left]] -= 1
                left += 1
        return '' if ans_left < 0 else s[ans_left: ans_right+1]


if __name__ == '__main__':
    solution = Solution()
    rst = solution.minWindow("ADOBECODEBANC", "ABC")
    print(rst)
