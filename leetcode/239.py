from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    left = 0
    maxNum = -1001

    while k <= len(nums):
        for i in nums[left:k]:
            maxNum = max(maxNum, i)
        res.append(maxNum)
        maxNum = -1001
        left += 1
        k += 1
    return res


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

#better solution
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    res = []
    q = deque()

    for idx, num in enumerate(nums):
        while q and q[-1] < num:
            q.pop()
        q.append(num)

        if idx >= k and nums[idx - k] == q[0]:
            q.popleft()
        
        if idx >= k - 1:
            res.append(q[0])
    
    return res