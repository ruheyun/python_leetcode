# coding:UTF-8
# @Author:RuHe
# @Time:2024/12/14 19:58
import numpy as np

def experiment(n, t):
    wealth = np.array([100 for i in range(n)])
    for i in range(t):
        for j in range(n):
            if wealth[j] > 0:
                while True:
                    ind = np.random.randint(0, 100)
                    if ind != j:
                        break
                wealth[j] -= 1
                wealth[ind] += 1
    print(f'{n}个人的财富从小到大排序为\n{np.sort(wealth)}，\n该社会基尼系数为{calculate_gini(wealth)}')


def calculate_gini(wealth):
    sum_abs_differences = 0
    sum_wealth = np.sum(wealth)
    for i in range(len(wealth)):
        sum_abs_differences += np.sum(np.abs(wealth - wealth[i]))
    return sum_abs_differences / (2 * len(wealth) * sum_wealth)


if __name__ == '__main__':
    n = 100
    t = 100000
    experiment(n, t)