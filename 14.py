import typing


class Solution:
    def longestCommonPrefix(self, strs: typing.List[str]) -> str:
        prefix = ""
        c = 0

        while c < len(strs[0]):
            char = strs[0][c]

            for s in strs[1:]:
                if c == len(s) or s[c] != char:
                    return prefix

            prefix += char
            c += 1

        return prefix
