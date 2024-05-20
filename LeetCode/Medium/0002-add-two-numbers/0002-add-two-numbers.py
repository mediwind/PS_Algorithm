# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 정답을 담을 연결 리스트
        dummy = ListNode()
        cur = dummy

        # 각 노드의 합이 두자리 수인 경우 둘째 자리를 다음 자리수로 넘길 변수 carry
        carry = 0
        # 7 + 8 처럼 자리수가 하나 더 추가될 경우를 대비해 carry 역시 조건문으로
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next