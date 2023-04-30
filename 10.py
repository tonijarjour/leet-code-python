class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*" or p == s or (p == "." and len(s) == 1):
            return True

        svec = [c for c in s]
        pvec = [c for c in p]

        byStars = []

        while pvec and (
            pvec[-1] == "." or (svec and pvec[-1] == svec[-1]) or (pvec[-1] == "*")
        ):
            if pvec[-1] == "*":
                if svec and (pvec[-2] == svec[-1] or pvec[-2] == "."):
                    byStars.append(svec.pop())
                else:
                    pvec.pop()
                    last = pvec.pop()
                    if last == ".":
                        while pvec and pvec[-1] == ".":
                            pvec.pop()

            else:
                pvec.pop()
                if not svec:
                    return False
                svec.pop()

        if not pvec:
            if svec:
                return False
            return True

        pvec.reverse()
        if byStars and byStars[len(pvec) * -1 :] == pvec and not svec:
            return True

        return False


s = Solution()
