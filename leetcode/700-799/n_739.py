"""
739. 每日温度
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m = temperatures[-1]
        n = len(temperatures)
        lst = [0] * n
        for i in range(len(temperatures) - 1, -1, -1):
            if temperatures[i] >= m:
                lst[i] = 0
                m = temperatures[i]
                continue

            for j in range(i + 1, n):
                if temperatures[i] == temperatures[j]:
                    lst[i] = lst[j] + j - i
                    break
                lst[i] += 1
                if temperatures[i] < temperatures[j]:
                    break
        return lst


