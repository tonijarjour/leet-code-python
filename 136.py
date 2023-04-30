import typing


class Solution:
    def singleNumber(self, nums: typing.List[int]) -> int:
        uniques = set()

        for n in nums:
            if n not in uniques:
                uniques.add(n)
            else:
                uniques.remove(n)

        return uniques.pop()
