"""
Docstring for leetcode.n_258 各位相加
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        return self.addDigits(num // 10 + num % 10)
    
    def addDigits_(self, num: int) -> int:
        ans = num
        while True:
            if ans < 10:
                return ans
            ans = num // 10 + num % 10
            num = ans
    
    def addDigits_a(self, num: int) -> int:
        return 9 if num % 9 == 0 and num >= 9 else num % 9