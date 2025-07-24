def mySqrt(x: int) -> int:
    for i in range(x+1):
        if i*i > x:
            return i-1
    if x == 0 or x == 1:
        return x

print(mySqrt(2))


#best solution
def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    ans = 0

    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans
