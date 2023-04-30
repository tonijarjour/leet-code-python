import typing


class Solution:
    def reverseString(self, s: typing.List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s) // 2):
            s[i], s[0 - i - 1] = s[0 - i - 1], s[i]
