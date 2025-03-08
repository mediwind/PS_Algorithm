# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 더미 노드를 생성하여 리스트의 시작 부분을 가리키게 함
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            # 교환할 두 노드를 지정
            first = current.next
            second = current.next.next
            
            # 노드 교환
            first.next = second.next
            second.next = first
            current.next = second
            
            # 포인터를 두 노드 앞으로 이동
            current = first
        
        return dummy.next