from typing import List


def majorityElement(nums: List[int]) -> int:
    hasher = {}

    for i in nums:
        if i not in hasher:
            hasher[i] = 0
        hasher[i]  += 1
    return list(dict(sorted(hasher.items(), key=lambda item: item[1], reverse=True)))[0]

print(majorityElement([2,2,1,1,1,2,2]))