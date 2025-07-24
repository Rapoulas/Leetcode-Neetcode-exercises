from typing import List


def removeDuplicates(nums: List[int]) -> int:
    seen = set()
    i = 0
    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[i] = num
            i += 1
    return (i, nums[:i])


result = removeDuplicates([1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 6])
print(result[0], result[1])