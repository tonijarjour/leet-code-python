class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        curr = 0

        values = {
            "M": 1000,
            "D": 500,
            "L": 50,
            "V": 5,
            "C": 100,
            "X": 10,
            "I": 1,
        }

        prefix = {
            "C": {
                "D": 300,
                "M": 800,
            },
            "X": {
                "L": 30,
                "C": 80,
            },
            "I": {
                "V": 3,
                "X": 8,
            },
        }

        while curr < len(s):
            sum += values[s[curr]]
            if curr == len(s) - 1:
                break

            sufval = prefix.get(s[curr], {"": 0}).get(s[curr + 1], 0)
            if sufval > 0:
                sum += sufval
                curr += 1

            curr += 1

        return sum
