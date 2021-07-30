"""
3.无重复字符的最长字串
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
示例1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        max_len = 0
        cur_len = 0
        max_str = ''
        for i in range(n):
            cur_len += 1
            while s[i] in max_str:
                max_str = max_str[1:]
                cur_len -= 1
            max_len = max(max_len, cur_len)
            max_str += s[i]
        return max_len


"""
53.最大子序和
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_list = []
        max_sum = nums[0]
        cur_sum = nums[0]
        if n == 1:
            return nums[0]
        for i in range(1, n):
            if cur_sum < 0:
                cur_sum = nums[i]
                max_list = [nums[i]]
                i += 1
            elif cur_sum >= 0:
                max_list.append(nums[i])
                cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        print(max_list)
        return max_sum
