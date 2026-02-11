"""
Docstring for leetcode.n_14
最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a, b = min(strs), max(strs)
        for i in range(len(a)):
            if a[i] != b[i]:
                return a[:i]
        return a