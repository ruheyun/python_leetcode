"""
Docstring for leetcode.n_2469 温度转换
"""
from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        return [kelvin, fahrenheit]
    
# 直接计算