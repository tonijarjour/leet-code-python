class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}

        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1

            if t[i] in chars:
                chars[t[i]] -= 1
            else:
                chars[t[i]] = -1

        return all(c == 0 for c in chars.values())


ins = Solution()
ins.isAnagram("hello", "elloh")
