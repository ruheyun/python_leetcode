"""
Docstring for leetcode.n_1281 整数的各位积和之差
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while True:
            if n // 10 == 0:
                return product * n - (sum + n)
            num = n % 10
            n //= 10
            product *= num
            sum += num