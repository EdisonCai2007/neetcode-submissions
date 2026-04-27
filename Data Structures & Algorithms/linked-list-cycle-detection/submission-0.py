# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()

        while (head not in hashset):
            hashset.add(head)
            
            if (not head.next):
                return False
            head = head.next

        return True