from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    hasher = {}
    for i in nums:
        if hasher.get(i) is not None:
            hasher[i] += 1
        else:
            hasher[i] = 1
    return list(dict(sorted(hasher.items(), key=lambda item: item[1], reverse=True)))[:k]

print(topKFrequent([1,2,2,2,2,2,3,3,3], 2))