import typing


class Solution:
    def findMedianSortedArrays(
        self, nums1: typing.List[int], nums2: typing.List[int]
    ) -> float:
        def findMedian(l):
            if len(l) % 2 == 0:
                mid = (len(l) - 1) // 2
                return (l[mid] + l[mid + 1]) / 2.0

            return l[(len(l) - 1) // 2]

        if not nums1 or not nums2:
            return findMedian(nums1 or nums2)

        if nums1[0] >= nums2[-1]:
            nums1 = nums2 + nums1
            return findMedian(nums1)
        elif nums2[0] >= nums1[-1]:
            nums1 += nums2
            return findMedian(nums1)

        while nums2:
            n = nums2.pop()

            left = 0
            right = len(nums1) - 1

            while left <= right:
                mid = (left + right) // 2

                if mid == 0 and n < nums1[0]:
                    nums1.insert(0, n)
                    break
                elif mid == len(nums1) - 1 and n > nums1[-1]:
                    nums1.append(n)
                    break
                elif n <= nums1[mid]:
                    if n < nums1[mid - 1]:
                        right = mid - 1
                    else:
                        nums1.insert(mid, n)
                        break
                elif n > nums1[mid]:
                    if n > nums1[mid + 1]:
                        left = mid + 1
                    else:
                        nums1.insert(mid + 1, n)
                        break

        return findMedian(nums1)


l1 = [1, 2, 4]
l2 = [3]

s = Solution()
print(s.findMedianSortedArrays(l1, l2))
