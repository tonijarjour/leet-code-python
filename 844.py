class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def intoStack(i):
            stack = []
            for c in i:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()

            return stack

        return intoStack(s) == intoStack(t)
