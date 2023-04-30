import typing


class Solution:
    def missingNumber(self, nums: typing.List[int]) -> int:
        total = sum(nums)
        lo = nums[0]
        hi = nums[0]

        for n in nums[1:]:
            if n < lo:
                lo = n
            if n > hi:
                hi = n

        if hi != len(nums):
            return len(nums)
        return sum(range(lo, hi + 1)) - total
