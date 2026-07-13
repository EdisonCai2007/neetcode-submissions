# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half (split lists)
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # merge halves
        first, second = head, prev

        while second:
            temp = first.next
            first.next = second
            first = temp
            temp = second.next
            second.next = first
            second = temp


#           I
# 1 -> 2 -> 3 -> 4 -> None
#      S         F

# 1 -> 2 -> None
#      ^
# 4 -> 3 -> None
#      ^

# 1 -> 4 -> 2 -> 3