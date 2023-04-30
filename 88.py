import typing


class Solution:
    def merge(
        self, nums1: typing.List[int], m: int, nums2: typing.List[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while nums1 and nums1[-1] == 0 and len(nums1) > m:
            nums1.pop()

        if not nums1:
            nums1[:] = nums2
        elif nums2 and nums1[0] >= nums2[-1]:
            nums1[:] = nums2 + nums1
        elif nums2 and nums2[0] >= nums1[-1]:
            nums1 += nums2
        elif nums2:
            while nums2:
                curr = nums2.pop()

                left = 0
                right = len(nums1) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if mid == 0 and curr <= nums1[0]:
                        nums1.insert(0, curr)
                        break
                    elif mid == len(nums1) - 1 and curr >= nums1[-1]:
                        nums1.append(curr)
                        break
                    elif curr <= nums1[mid]:
                        if curr < nums1[mid - 1]:
                            right = mid - 1
                        else:
                            nums1.insert(mid, curr)
                            break
                    elif curr > nums1[mid]:
                        if curr > nums1[mid + 1]:
                            left = mid + 1
                        else:
                            nums1.insert(mid + 1, curr)
                            break


s = Solution()
s.merge([2, 0], 1, [1], 1)
