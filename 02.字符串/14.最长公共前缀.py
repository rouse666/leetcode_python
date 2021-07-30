"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        length = len(strs[0])
        count = len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(count):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]
