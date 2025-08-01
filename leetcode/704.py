from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1

    while l <= r:
        mid = (l + r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(search([-1,0,2,4,6,8], 3))