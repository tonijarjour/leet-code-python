class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nchars = set(needle)
        if haystack == needle:
            return 0

        n = 0
        while n <= len(haystack) - len(needle):
            substr = haystack[n : n + len(needle)]

            if needle == substr:
                return n

            n += max(len(nchars.difference(set(substr))), 1)

        return -1


s = Solution()
print(s.strStr("hello", "ll"))
