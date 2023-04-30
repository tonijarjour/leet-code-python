import typing


class Solution:
    def moveZeroes(self, nums: typing.List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        nums[:] = [n for n in nums if n != 0]
        nums.extend([0 for _ in range(nlen - len(nums))])
