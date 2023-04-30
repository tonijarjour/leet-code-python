# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = right = head

        while right and right.next:
            right = right.next.next
            mid = mid.next

        node = None

        while mid:
            child = mid.next
            mid.next = node
            node = mid
            mid = child

        while node:
            if node.val != head.val:
                return False

            node = node.next
            head = head.next
        return True
