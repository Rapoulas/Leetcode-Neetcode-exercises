from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if target in nums:
        for i in range(nums.index(target), len(nums)-1):
            if nums[i] != nums[i+1]:
                return [nums.index(target), i]
        return [nums.index(target), len(nums)-1]
    return [-1, -1]

print(searchRange([5,7,7,8,8,10], 6))