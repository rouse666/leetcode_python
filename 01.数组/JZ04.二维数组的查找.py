# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 从右上角往下找，>就消除所在行继续向下，<就消除所在列
        for i in range(len(array)):
            for j in range(len(array[0])):
                if target < array[i][j]:
                    j -= 1
                    continue
                elif target > array[i][j]:
                    i -= 1
                    continue
                elif target == array[i][j]:
                    return True
