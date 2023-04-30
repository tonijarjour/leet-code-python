import typing


class Solution:
    def intersect(
        self, nums1: typing.List[int], nums2: typing.List[int]
    ) -> typing.List[int]:
        map = {}

        for n in nums1:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1

        result = []

        for n in nums2:
            if n in map and map[n] > 0:
                map[n] -= 1
                result.append(n)

        return result
