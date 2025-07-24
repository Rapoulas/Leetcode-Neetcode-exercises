from typing import List


def trap(height: List[int]) -> int:
    l, r = 0, len(height)-1
    res = 0
    leftMax, rightMax = height[l], height[r]

    while l < r:
        if leftMax <= rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

print(trap([0,2,0,3,1,0,1,3,2,1]))