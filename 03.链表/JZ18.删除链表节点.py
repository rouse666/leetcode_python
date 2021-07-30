# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            head = head.next
            return head
        p = head
        while p.next.val != val:
            p = p.next
        p.next = p.next.next
        return head
