"""
Docstring for leetcode.n_263 丑数
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        flag = True
        while flag and n > 5:
            flag = False
            if n % 2 == 0:
                n //= 2
                flag = True
            if n % 3 == 0:
                n //= 3
                flag = True
            if n % 5 == 0:
                n //= 5
                flag = True
        return True if 1 <= n <= 5 else False
            
        