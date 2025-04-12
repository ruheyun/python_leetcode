# coding:UTF-8
# RuHe  2025/4/12 10:55
# 找到字符串中所有字母异位词
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)
        print(cnt)
        return ans


if __name__ == '__main__':
    solution = Solution()
    ls = solution.findAnagrams("fecbaebabacd", "abc")
    print(ls)


