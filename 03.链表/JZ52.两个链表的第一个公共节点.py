# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 思路：首先我们要知道什么是公共节点，
# 两个链表从某一节点开始，他们的next都指向同一个节点。
# 但由于是单向链表的节点，每个节点只有一个next，因此从第一个公共节点开始，之后他们的所有节点都是重合的，不可能再出现分叉。
# 所以可以先遍历两个链表得到他们的长度，就能知道哪个链表比较长，以及长的链表比短的链表多几个结点。
# 在第二次遍历的时候，在较长的链表上先走若干步，接着同时在两个链表上遍历，找到的第一个相同的结点就是他们的第一个公共结点。
# 时间复杂度为O(m+n)，而暴力破解法的时间复杂度为O(mn).
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        listA = []
        if not pHead1 or not pHead2:
            return None
        while pHead1:
            listA.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2 in listA:
                return pHead2
            pHead2 = pHead2.next
        return None
