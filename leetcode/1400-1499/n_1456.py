"""
Docstring for leetcode.1400-1499.n_1456 定长子串中元音的最大数目
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_ans = ans = 0
        j = 0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                ans += 1
            if i - j + 1 == k:
                if j != 0 and s[j - 1] in 'aeiou':
                    ans -= 1
                max_ans = max(max_ans, ans)
                if max_ans == k:
                    break
                j += 1
        return max_ans
    

sol = Solution()
result = sol.maxVowels("abciiidef", 3)
print(result)