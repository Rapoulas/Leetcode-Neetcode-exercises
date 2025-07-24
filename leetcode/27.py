from typing import List


def removeElement(nums: List[int], val: int) -> int:
    k = 1
    if len(nums) > 0:
        while (k-1 != len(nums)):
            if nums[k-1] is val:
                nums.pop(k-1)
            else:
                k += 1
    return [k, nums]

ans = removeElement([3,2,2,3], 3)
print(ans[0], ans[1])