# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        if pHead1.val < pHead2.val:
            mergehead = pHead1
            mergehead.next = self.Merge(pHead1.next, pHead2)
        else:
            mergehead = pHead2
            mergehead.next = self.Merge(pHead1, pHead2.next)
        return mergehead
