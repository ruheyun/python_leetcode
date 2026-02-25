"""
2269. 找到一个数字的 K 美丽值
"""

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        div = 10 ** k
        n = num
        while n >= div / 10:
            m = n % div
            n = n // 10
            if m != 0 and num % m == 0:
                ans += 1
        return ans
    
Solution().divisorSubstrings(240, 2)
