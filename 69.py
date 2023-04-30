class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1

        right = x // 2 + 1
        left = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x or (mid * mid < x and (mid + 1) * (mid + 1) > x):
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return 0
