# class Solution:
#     def fib(self, n: int) -> int:
#         if n<=1:
#             return n
#         else:
#             return self.fib(n-1)+self.fib(n-2)

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a % 1000000007


"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
示例 1：
输入：n = 2
输出：2
"""


class Solution:
    def numWays(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n):
            a, b = b, a + b
        return a % 1000000007
