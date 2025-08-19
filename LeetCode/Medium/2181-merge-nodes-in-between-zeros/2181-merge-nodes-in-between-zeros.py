# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        cur = head.next  # 첫 노드는 0이므로 그 다음부터 시작
        s = 0
        while cur:
            if cur.val == 0:
                # 구간 끝: 누적합으로 새 노드 추가
                tail.next = ListNode(s)
                tail = tail.next
                s = 0
            else:
                s += cur.val
            cur = cur.next
        return dummy.next