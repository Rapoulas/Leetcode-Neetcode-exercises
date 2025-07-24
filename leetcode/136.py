from typing import List


def singleNumber(nums: List[int]) -> int:
    hasher = {}
    for i in nums:
        if i not in hasher:
            hasher[i] = 0
        hasher[i] += 1
    return list(dict(sorted(hasher.items(), key=lambda item: item[1])))[0]

print(singleNumber([2,2,1, 3, 3, 3, 1, 4]))

#best solution
def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return nums[result]

print(singleNumber([2,2,1, 3, 3, 3, 1, 4]))