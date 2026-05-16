# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        # iterate through both list1 and list2
        while list1 and list2:
            if list1.val <= list2.val:
                # take the minimum node and add to curr.next
                curr.next = list1
                
                # move pointer
                list1, curr = list1.next, curr.next
            else:
                curr.next = list2
                list2, curr = list2.next, curr.next
        
        # add remaining list to curr.next
        if not list1: # list1 is empty
            curr.next = list2
        else: # list 2 is empty
            curr.next = list1

        return head.next
