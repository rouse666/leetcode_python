"""
给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积，它们的乘积也表示为字符串形式。

示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))