from typing import List


def maxArea(heights: List[int]) -> int:
    l, r = 0, len(heights)-1
    res = 0

    while l < r:
        maxWater = min(heights[l], heights[r]) * (r-l)
        res = maxWater if maxWater > res else res

        if heights[l] > heights[r]:
            r -= 1
        elif heights[l] <= heights[r]:
            l += 1
    return res

print(maxArea([1,7,2,5,4,7,3,6]))