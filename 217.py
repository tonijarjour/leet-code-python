import typing


class Solution:
    def containsDuplicate(self, nums: typing.List[int]) -> bool:
        uniq = set()

        for n in nums:
            if n not in uniq:
                uniq.add(n)
            else:
                return True

        return False
