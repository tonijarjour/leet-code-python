# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        a = ""
        b = ""

        while l1:
            a += str(l1.val)
            l1 = l1.next

        while l2:
            b += str(l2.val)
            l2 = l2.next

        a = int("".join(reversed(a)))
        b = int("".join(reversed(b)))

        out = a + b
        out = "".join(reversed(str(out)))

        curr = head = ListNode(int(out[0]))

        for d in out[1:]:
            curr.next = ListNode(int(d))
            curr = curr.next

        return head
