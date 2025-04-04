from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    count = 0
    max = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    return max if max > count else count


print(findMaxConsecutiveOnes([1,1,0,1,1,1]))