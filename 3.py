class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = {}
        longest = 0
        length = 0
        curr = 0

        while curr < len(s):
            if s[curr] not in uniq:
                length += 1
                uniq[s[curr]] = curr
            else:
                curr = uniq[s[curr]] + 1
                uniq.clear()
                uniq[s[curr]] = curr
                if length > longest:
                    longest = length
                length = 1

            curr += 1

        if length > longest:
            return length

        return longest
