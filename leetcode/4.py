from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    for i in nums2:
        nums1.append(i)
    nums1.sort()
    if len(nums1) % 2 == 0:
        return (nums1[len(nums1)//2] + nums1[len(nums1)//2-1]) / 2
    else:
        return nums1[len(nums1)//2]

print(findMedianSortedArrays([1, 3, 5], [2, 4, 6]))