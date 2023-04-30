class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq = {}
        dup = set()

        for i, c in enumerate(s):
            if c in uniq:
                del uniq[c]
                dup.add(c)
            if c not in dup:
                uniq[c] = i

        if not uniq:
            return -1
        return uniq[min(uniq)]
