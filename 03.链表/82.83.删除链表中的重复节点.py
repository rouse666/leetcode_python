"""
26.给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                # 如果快指针和慢指针所指的元素不相同，证明慢指针所指元素的重复已结束，索引 i + 1，并把新的元素赋给索引 i 处
                # 也就是说，慢指针记录的是非重复元素的索引，最后返回非重复元素个数为 i + 1
        return i + 1


# 2021.7.15
# [1,1,2]->[1,2]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


# [1,2,3,3,4,4,5]
# [1,2,5]
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplication(self, pHead):
        if not pHead:
            return pHead
        dummy = ListNode(0, pHead)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
