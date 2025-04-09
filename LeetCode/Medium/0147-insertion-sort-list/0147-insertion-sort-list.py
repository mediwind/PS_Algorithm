# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 정렬된 부분의 시작을 나타내는 더미 노드 생성
        dummy = ListNode(0)
        dummy.next = head
        current = head.next
        head.next = None

        while current:
            # 삽입할 노드 추출
            temp = current
            current = current.next
            temp.next = None

            # 정렬된 리스트에서 삽입 위치 찾기
            prev = dummy
            while prev.next and prev.next.val < temp.val:
                prev = prev.next

            # 노드를 정렬된 리스트에 삽입
            temp.next = prev.next
            prev.next = temp

        return dummy.next