import typing


class Solution:
    def plusOne(self, digits: typing.List[int]) -> typing.List[int]:
        carry = 0

        if digits == [9]:
            return [1, 0]

        digits[-1] += 1
        if digits[-1] == 10:
            digits[-1] = 0
            carry = 1

        for n in range(len(digits) - 2, -1, -1):
            digits[n] += carry
            carry = 0
            if digits[n] == 10:
                digits[n] = 0
                carry = 1
            if n == 0 and carry == 1:
                digits.insert(0, 1)

        return digits
