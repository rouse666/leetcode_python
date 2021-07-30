# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点而不是节点的数值
    def __init__(self):
        self.res = []

    def KthNode(self, pRoot, k):
        self.dfs(pRoot)
        if 0 <= k <= len(self.res):
            return self.res[k - 1]
        else:
            return None

    def dfs(self, root):
        if not root:
            return None
        self.dfs(root.left)
        self.res.append(root)
        self.dfs(root.right)
