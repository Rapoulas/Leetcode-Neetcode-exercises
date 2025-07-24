from typing import List

#First solution
# def containsDuplicate(nums: List[int]) -> bool:
#     uniques = []
#     for i in nums:
#         if i in uniques:
#             return True
#         uniques.append(i)
#     return False

#Optimized solution
def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

print(containsDuplicate([1, 2, 3, 3]))