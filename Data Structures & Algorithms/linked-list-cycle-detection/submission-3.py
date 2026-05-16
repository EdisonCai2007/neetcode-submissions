# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            # move slow and fast
            slow = slow.next
            fast = fast.next.next

            # check if slow and fast equal
            if slow == fast:
                return True
        
        # end of cycle found, return false
        return False