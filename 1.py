import typing


class Solution:
    def twoSum(self, nums: typing.List[int], target: int) -> typing.List[int]:
        map = {}

        for i, n in enumerate(nums):
            if (target - n) in map:
                return [map[target - n], i]

            if n not in map:
                map[n] = i


l = [2, 7, 11, 15]
s = Solution()
print(s.twoSum(l, 9))
