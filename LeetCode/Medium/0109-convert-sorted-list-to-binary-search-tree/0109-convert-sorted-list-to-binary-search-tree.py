# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 중간 노드를 찾기 위한 보조 함수 (slow/fast pointer)
        def find_mid(left, right):
            slow = fast = left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next
            return slow

        def build(left, right):
            if left == right:
                return None
            mid = find_mid(left, right)
            node = TreeNode(mid.val)
            node.left = build(left, mid)
            node.right = build(mid.next, right)
            return node

        return build(head, None)