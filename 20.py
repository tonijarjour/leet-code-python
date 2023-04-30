class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                left = stack.pop()
                if ord(left) + 1 == ord(c) or ord(left) + 2 == ord(c):
                    continue
                return False

        if stack:
            return False
        return True
