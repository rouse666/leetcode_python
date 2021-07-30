"""
给定一个含有n个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组[4,3]是该条件下的长度最小的子数组。
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        print(minlen)
        left = 0
        right = 0
        while right < len(nums):
            cur_target = sum(nums[left:right + 1])
            if cur_target >= target:
                minlen = min(minlen, right + 1 - left)
                left += 1
            else:
                right += 1
        if minlen == float('inf'):
            return 0
        else:
            return minlen
