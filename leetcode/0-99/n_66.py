from typing import List

def plusOne(digits: List[int]) -> List[int]:
    i = len(digits)
    while i - 1 >= 0:
        digits[i - 1] = digits[i - 1] + 1
        if digits[i - 1] == 10:
            digits[i - 1] = 0
            if i - 1 == 0:
                digits.insert(0, 1)
        else:
            break
        i -= 1
    return digits


