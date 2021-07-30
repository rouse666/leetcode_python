# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self, pHead, k):
        former, latter = pHead, pHead
        for i in range(k):
            if former is None:
                return None
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter
