"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回0。

示例 1：
输入：[2,1,2]
输出：5
示例 2：

输入：[1,2,1]
输出：0
示例 3：

输入：[3,2,3,4]
输出：10
示例 4：

输入：[3,6,2,3]
输出：8
"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # m=max(nums)
        # n=min(nums)
        n = len(nums)
        if n < 3:
            return 0
        # n-3-k>=0 k<=n-3 所以range(n-2)
        for k in range(n - 2):
            if (nums[n - 3 - k] + nums[n - 2 - k]) > nums[n - 1 - k] > (nums[n - 3 - k] - nums[n - 2 - k]):
                return nums[n - 3 - k] + nums[n - 2 - k] + nums[n - 1 - k]
        return 0
