class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        isneg = x < 0

        nstr = str(x if not isneg else x * -1)
        nstr = "".join(reversed(nstr))
        if int(nstr) > 0x7FFFFFFF:
            return 0

        if isneg:
            return -int(nstr)
        return int(nstr)
