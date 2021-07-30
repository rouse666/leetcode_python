"""
如果一个由'0' 和 '1'组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调递增的。
我们给出一个由字符 '0' 和 '1'组成的字符串S，我们可以将任何'0' 翻转为'1'或者将'1'翻转为'0'。
返回使 S 单调递增的最小翻转次数。

示例 1：
输入："00110"
输出：1
解释：我们翻转最后一位得到 00111.
"""


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        # 计算处于0左边的1，以及处于1右边的0的个数
        count1, flipCount = 0, 0
        for i in range(len(S)):
            if S[i] == '0':
                if count1 == 0:
                    continue
                else:
                    flipCount += 1
            else:
                count1 += 1
            flipCount = min(flipCount, count1)
        return flipCount
