"""
给定一个m x n二维字符网格board和一个字符串单词word.如果word存在于网格中，返回true；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 遍历矩阵，分别以每一个元素为起点开始深度遍历；
        # 若索引超出范围或当前元素不匹配，返回False；
        # 若当前元素匹配，则将当前元素标记为已访问，并递归遍历矩阵中下一个（上下左右四个方向）元素，即往深处遍历；
        # 若某一元素不匹配，回溯（当前元素标记为未访问），选取下一个元素为起点DFS；
        # 递归边界：单词中所有字母均匹配。
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board: List[List[str]], i: int, j: int, word: str) -> bool:
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'
        if self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i, j + 1,
                                                                                                  word[1:]) or self.dfs(
            board, i, j - 1, word[1:]):
            return True

        board[i][j] = tmp
        return False
