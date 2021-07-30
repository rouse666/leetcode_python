"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"
"""


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str, nums))

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return str(int("".join(nums)))
