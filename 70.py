class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev, curr = 1, 2

        for _ in range(2, n):
            hold = prev
            prev = curr
            curr = prev + hold

        return curr
