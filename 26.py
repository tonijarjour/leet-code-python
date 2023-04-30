class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        prev = None
        while n < len(nums):
            if nums[n] != prev:
                prev = nums[n]
            else:
                nums.pop(n)
                n -= 1

            n += 1

        return len(nums)
