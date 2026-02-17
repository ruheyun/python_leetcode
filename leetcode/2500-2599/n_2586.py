"""
Docstring for leetcode.2500-2599.n_2586 统计范围内的元音字符串数
"""
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = 'aeiou'
        ans = 0
        for word in words[left: right + 1]:
            if word[0] in vowels and word[-1] in vowels:
                ans += 1
        return ans
    

sol = Solution()
result = sol.vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4)
print(result)