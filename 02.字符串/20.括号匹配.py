# 字节一面2021.7.21
SYMBOLS = {')': '('}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()

def check(s):
    arr = []
    count = 0
    for c in s:
        if c in SYMBOLS_L:
            # 左符号入栈
            arr.append(c)
        elif c in SYMBOLS_R:
            # 右符号要么出栈，要么匹配失败
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
                count += 1
            else:
                count += 0
    return count

print(check('h)e(dh()ei9()34(39))'))

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {"}": "{", ")": "(", "]": "["}
        stack = list()
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack