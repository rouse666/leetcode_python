"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
"""


# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         set1=set(nums1)
#         set2=set(nums2)
#         return self.set_intersection(set1,set2)

#     def set_intersection(self,set1,set2):
#         if len(set1)>len(set2):
#             return self.set_intersection(set2,set1)
#         return [x for x in set1 if x in set2]


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1=set(nums1)
        list2=set(nums2)
        return [x for x in list1 if x in list2]