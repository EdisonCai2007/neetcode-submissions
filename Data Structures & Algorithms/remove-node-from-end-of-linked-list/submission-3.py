# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # remove element
        if length == n:
            head = head.next
            return head

        index = 0
        curr = head
        while curr:
            if index == length - n - 1:
                curr.next = curr.next.next
                return head
            index += 1
            curr = curr.next
