# coding:UTF-8
# RuHe  2025/4/5 10:35
# 字母异位词分组
from collections import defaultdict
from typing import List


class Solution:
    """
    时间复杂度：nmlogm
    空间复杂度：nm
    n：为strs的长度
    m：为strs[i]的长度
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return list(d.values())


if __name__ == '__main__':
    solution = Solution()
    lst = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(lst)