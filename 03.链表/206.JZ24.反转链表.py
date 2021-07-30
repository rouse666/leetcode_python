# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        nex = None
        pre = None
        while pHead:
            nex = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = nex
        return pre
