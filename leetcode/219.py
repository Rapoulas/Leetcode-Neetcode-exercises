from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    hmap={}
    for idx,val in enumerate(nums):
        if val in hmap and abs(hmap[val]-idx)<=k:
            return True
        hmap[val]=idx
    return False

print(containsNearbyDuplicate([1, 0, 1, 1], 1))