from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    arr = []
    for idx1, i in enumerate(nums):
        res = 1
        for idx2, j in enumerate(nums):
            if idx1 != idx2:
                res *= j
        arr.append(res)
    return arr

print(productExceptSelf([1,2,4,6]))