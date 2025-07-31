from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    searchArr = []
    for arr in matrix:
        if arr[-1] == target:
            return True
        elif arr[-1] > target:
            searchArr = arr
            break
    
    l, r = 0, len(searchArr)-1

    while l <= r:
        mid = (l + r)//2
        if searchArr[mid] == target:
            return True
        elif searchArr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))