from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i in range(m, n+m-1):
        nums1[i] = nums2[i-m]
    nums1.sort()

merge([1,2,4,5,6,0], 5, [3, 4], 2)