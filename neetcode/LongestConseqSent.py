from typing import List


def longestConsecutive(nums: List[int]) -> int:
    longestSeq, i, score = 0, 0, 1
    numSet = set(nums)
    numSet = sorted(list(numSet))
    if len(numSet) == 1:
        return 1
    while i < len(numSet)-1:
        if list(numSet)[i]+1 == list(numSet)[i+1]:
            score += 1
            if score > longestSeq:
                longestSeq = score
        else:
            score = 1
        i += 1
    return longestSeq

print(longestConsecutive([0, -1]))

#best solution
def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if (n-1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

print(longestConsecutive([0, -1]))