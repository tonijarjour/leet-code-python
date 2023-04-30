import typing


class Solution:
    def fizzBuzz(self, n: int) -> typing.List[str]:
        answer = []
        buffer = ""

        for i in range(1, n + 1):
            if i % 3 == 0:
                buffer += "Fizz"
            if i % 5 == 0:
                buffer += "Buzz"
            if i % 5 != 0 and i % 3 != 0:
                buffer += str(i)

            answer.append(buffer)
            buffer = ""

        return answer


s = Solution()
print(s.fizzBuzz(3))
