import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2

        time = 0
        for p in piles:
            time += math.ceil(float(p) / k)
        if time <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res
            
        

print(minEatingSpeed([1,10,3,2], 9))