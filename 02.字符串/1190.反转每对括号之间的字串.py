"""
给出一个字符串s（仅含有小写英文字母和括号）。
请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
注意，您的结果中 不应 包含任何括号。
示例 1：
输入：s = "(abcd)"
输出："dcba"
示例 2：
输入：s = "(u(love)i)"
输出："iloveu"
解释：先反转子字符串 "love" ，然后反转整个字符串。
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 反转最内层，去掉最内层括号
        # 反转第二层，去掉第二层括号
        ans = ['']
        for c in s:
            if c == '(':
                ans += ['']
            elif c == ')':
                ans[-2] += ans[-1][::-1]
                ans.pop()
            else:
                ans[-1] += c

            print(ans)
        return ans[0]