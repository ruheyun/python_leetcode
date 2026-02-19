"""
Docstring for leetcode.2300-2399.n_2379 得到 K 个黑块的最少涂色次数
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s = 0
        min_s = float('inf')
        for i in range(len(blocks)):
            s += int(blocks[i] == 'W')
            if i - k + 1 >= 0:
                min_s = min(min_s, s)
                if min_s == 0:
                    break
                s -= int(blocks[i - k + 1] == 'W')
        return min_s


# 上面不需要手动写 int 进行类型转换，会强制类型转换