import typing


class Solution:
    def maxProfit(self, prices: typing.List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for p in prices[1:]:
            if p < lowest:
                lowest = p
            if p <= profit:
                continue
            if p - lowest > profit:
                profit = p - lowest

        return profit
