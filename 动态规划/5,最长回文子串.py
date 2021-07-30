"""
给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：
输入：s = "cbbd"
输出："bb"
示例 3：
输入：s = "a"
输出："a"
示例 4：
输入：s = "ac"
输出："a"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        # 特殊处理
        if size == 1:
            return s
        # 创建动态规划表
        dp = [[False for _ in range(size)] for _ in range(size)]
        # 初始长度为1
        max_len = 1
        start = 0
        for j in range(1, size):
            for i in range(j):
                # 边界条件
                # 只有头尾相等
                if j - i <= 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        cur_len = j - i + 1

                # 状态转移方程
                # 当前dp[i][j]状态，头尾相等
                # 过去dp[i][j]状态,去掉头尾之后还是回文
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                        cur_len = j - i + 1
                # 出现回文更新输出
                if dp[i][j]:
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        # 输出内容
        return s[start:start + max_len]