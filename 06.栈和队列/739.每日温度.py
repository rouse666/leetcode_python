"""
请根据每日气温列表 temperatures，请计算在每一天需要等几天才会有更高的温度。如果气温在这之后都不会升高，请在该位置用0来代替。
示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出:[1,1,4,2,1,1,0,0]
示例 2:
输入: temperatures = [30,40,50,60]
输出:[1,1,1,0]
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        print(res)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                print(stack[-1])
                print(temperatures[stack[-1]])
                idx = stack.pop()
                print(idx)
                res[idx] = i - idx
            stack.append(i)
        return res
