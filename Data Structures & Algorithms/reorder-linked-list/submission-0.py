# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        deq = deque()

        if head is None:
            return

        curr = head.next;
        while curr is not None:
            deq.append(curr)
            curr = curr.next

        curr = head;
        while deq:
            curr.next = deq.pop()
            curr = curr.next
            if deq:
                curr.next = deq.popleft()
                curr = curr.next
        curr.next = None
