# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        # Traverse the list
        while current and current.next:
            # If the current value is the same as the next value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        
        return head