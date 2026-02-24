"""
567. 字符串的排列
"""
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        dit1 = defaultdict(int)
        for s in s1:
            dit1[s] += 1
        for i in range(n2):
            if s2[i] in s1:
                dit1[s2[i]] -= 1
                if dit1[s2[i]] == 0:
                    del dit1[s2[i]]
            
            if i - n1 + 1 >= 0:
                if len(dit1) == 0:
                    return True
                if s2[i - n1 + 1] in s1:
                    dit1[s2[i - n1 + 1]] += 1
                    if dit1[s2[i - n1 + 1]] == 0:
                        del dit1[s2[i - n1 + 1]]
        return False


sol = Solution()
result = sol.checkInclusion("adc", "dcda")
print(result)